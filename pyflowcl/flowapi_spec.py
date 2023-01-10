# pyflowcl/flowapi_spec.py
"""
Entrega funciones de procesamiento de la API de Flow Chile para procesamiento de pagos.

Este modulo contiene

- `FlowAPI` - Objeto Principal
- `load_yaml_file(yaml_file)` - Funcion para leer archivos YAML

__Uso Básico__:
```python
from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(flow_key="api_key", flow_secret="api_secret")
parametros = {"apiKey": api.apiKey, "token": "TOKEN_PAGO"}
api.objetos.call_get_payment_getstatus(
    parameters=genera_parametros(parametros, api.secretKey)
)
```

__Para ver una lista de operaciones disponibles__:
```python
from pyflowcl import FlowAPI

api = FlowAPI(flow_key="api_key", flow_secret="api_secret")
api.listar_operaciones()
```



"""
from typing import Any, Optional
from dataclasses import dataclass, field
from openapi3 import OpenAPI
import yaml
import os
from pyflowcl.exceptions import ConfigException
from functools import lru_cache
import fsutil
import logging
from slugify import slugify
import logging
from pathlib import Path


@dataclass
class FlowAPI(object):
    """
    Objeto principal, puede ser instanciado o heredado.

    Implementa todos los métodos de ``dataclass``.

    Attributes:
        flow_key: APIKey entregado por Flow
        flow_secret: SecretKey entregado por Flow
        flow_use_sandbox: True para usar `sandbox`, False o indefinido para `live`
        flow_yaml_file: Ruta alternativa a la especificacion OpenAPI, no puede ser usada en conjunto con `FlowAPI.flow_use_sandbox`.
        flow_yaml_spec: Objeto YAML de flow_yaml_file
        fix_openapi: ver `FlowAPI.fix_openapi3()`
    """

    base_path: Any = Path(__file__).resolve().parent
    _openapi3: Optional[OpenAPI] = field(init=False)
    flow_key: str = None
    flow_secret: str = None
    flow_yaml_file: str = None
    flow_yaml_spec: dict = field(repr=False, default=None)
    flow_use_sandbox: bool = False
    fix_openapi: bool = True

    def __post_init__(self):
        """Procesos post inicio

        Define las variables dentro del objeto, ejecuta inicializacion de configuraciones
        """

        if not self.flow_key:
            self.flow_key = os.getenv("PYFLOWCL_KEY", None)
        if not self.flow_secret:
            self.flow_secret = os.getenv("PYFLOWCL_SECRET", None)
        if not self.flow_use_sandbox:
            val = os.getenv("PYFLOWCL_USE_SANDBOX", "False")
            self.flow_use_sandbox = True if (val.lower() == "true") else False
            del val
        if not self.flow_yaml_file:
            self.flow_yaml_file = os.getenv("PYFLOWCL_YAML_FILE", None)
        if not self.fix_openapi:
            val = os.getenv("PYFLOWCL_FIX_OPENAPI", "True")
            self.fix_openapi = True if (val.lower() == "true") else False
            del val
        self._openapi3 = None

        self.init_api()

    def _define_archivo(self) -> None:
        if self.flow_yaml_file:
            return

        if self.flow_use_sandbox:
            self.flow_yaml_file = os.path.join(
                self.base_path, "yaml_files/apiFlow.sandbox.min.yaml"
            )
        else:
            self.flow_yaml_file = os.path.join(
                self.base_path, "yaml_files/apiFlow.min.yaml"
            )
        return

    def init_api(self) -> None:
        """
        Genera las validaciones y configuraciones necesarias para leer el
        archivo YAML con la especificacion.
        """
        self.check_config()
        self._define_archivo()
        self.load_yaml_spec(self.flow_yaml_file)

        # Flow no agrega operationId dentro de las propiedades de cada endpoint
        # Se crea uno para cada endpoint usando ``slugify``
        # `fix_it=False` para deshabilitar (por defecto en True)

        self.create_openapi3()

    @property
    def objetos(self) -> OpenAPI:
        """
        Entrega la instancia OpenAPI

        Returns:
            Objeto ``openapi3.OpenAPI``
        """
        return self._openapi3

    def lista_operaciones(self) -> list:
        """Lista operaciones disponibles

        Returns:
            Operaciones disponibles
        """
        return self._openapi3._operation_map.keys()

    @property
    def apiKey(self) -> str:
        """Retorna APIKey

        Returns:
            `apiKey`
        """
        return self.flow_key

    @property
    def secretKey(self) -> str:
        """Retorna SecretKey

        Returns:
            `SecretKey`
        """
        return self.flow_secret

    def check_config(self) -> bool:
        """
        Verifica que los datos de configuracion sean correctos.

        Se pueden definir desde la instancia

        ```python
        api = FlowAPI(flow_key="APIKey", flow_secret="SecretKey")
        ```
        o usando variables de entorno

        ```bash
        export PYFLOWCL_KEY="APIKey"
        export PYFLOWCL_SECRET="SecretKey"
        ```

        Returns:
            ``True`` si la validacion fue exitosa, ``False`` de lo contrario.

        Raises:
            ConfigException: Cuando falta un parametro por definir
        """

        if self.flow_use_sandbox and self.flow_yaml_file:
            raise ConfigException(
                "No se puede definir `flow_use_sandbox` y `flow_yaml_file`"
            )

        if not self.flow_key:
            error_msg = 'Se necesita configurar FLOW_KEY, puedes agregarlo al constructor: api = FlowAPI(key="secret_key") o como variable de entorno: export PYFLOWCL_KEY="secret_key" '
            raise ConfigException(error_msg)
            return False

        if not self.flow_secret:
            error_msg = 'Se necesita configurar FLOW_SECRET, puedes agregarlo al constructor api = FlowAPI(secret="secret") o como variable de entorno export PYFLOWCL_SECRET="secret" '
            raise ConfigException(error_msg)
            return False

        return True

    def load_yaml_spec(self, spec: str = None) -> None:
        """
        Carga el documento YAML como diccionario Python en ``FlowAPI.flow_yaml_spec``

        Args:
            spec: Cadena de texto con el documento YAML
            download: Descarga el archivo desde Flow en caso de no encontarse.
        Raises:
            Exception: Cuando ``spec`` no está definido
            OSError: Cuando no fue posible descargar el archivo YAML
        """
        if not spec:
            raise Exception("spec debe ser un documento/archivo YAML válido")
        try:
            self.flow_yaml_spec = load_yaml_file(spec)
        except OSError as e:
            raise e

    def create_openapi3(self, fix_it: bool = True) -> None:
        """
        Crea la instancia OpenAPI y la guarda en ``FlowAPI._openapi3``

        Args:
            fix_it: Soluciona en problema en la especificacion
        """
        if fix_it:
            self.fix_openapi3()
        api_spec = OpenAPI(self.flow_yaml_spec)
        self._openapi3 = api_spec

    def fix_openapi3(self):
        """
        Por defecto, Flow no entrega "operationId" en cada una de las operaciones
        esto provoca que no sea posible generar llamadas automaticas.
        Este método crea el valor "operationId" y lo actualiza directamente en
        ``FlowAPI.flow_yaml_spec``.
        El valor de cada operacion es generado con slugify siguiendo esta estructura

        Examples:
            >>> slugify("get /payment/getStatus", separator="_")
            'get_payment_getstatus'
        """
        for path in self.flow_yaml_spec["paths"]:
            for verb in self.flow_yaml_spec["paths"][path]:
                slug = None
                """
                Si Flow decide agregar los operationId, entonces nos los saltamos
                """
                if "operationId" not in self.flow_yaml_spec["paths"][path][verb]:
                    slug = slugify(f"{verb} {path}", separator="_")
                    self.flow_yaml_spec["paths"][path][verb]["operationId"] = slug


@lru_cache()
def load_yaml_file(yaml_file: str = None) -> Any:
    """
    Lee el archivo YAML desde el disco, ``lru_cache`` activado por defecto

    Args:
        yaml_file: Ruta con el archivo YAML a leer

    Returns:
        El archivo YAML procesado con ``yaml.safe_load()``

    Raises:
        OSError: El archivo indicado no existe

    """
    if not fsutil.is_file(yaml_file):
        raise OSError(f"El archivo {yaml_file} no existe.")

    with open(yaml_file) as f:
        """
        Se eliminan ``\\t`` ya que el archivo de flow tiene un error de formato
        """
        return yaml.safe_load(f.read().replace("\t", ""))
