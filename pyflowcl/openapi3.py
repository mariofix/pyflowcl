# pyflowcl/openapi3.py
"""
Entrega funciones de procesamiento de la API de Flow Chile.

Este modulo contiene

- `FlowAPI` - Objeto Principal
- `load_yaml_file(yaml_file)` - Funcion para leer archivos YAML

__Uso Básico__:
```python
from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(api_key="api_key", secret_key="api_secret")
parametros = {"apiKey": api.apiKey, "token": "TOKEN_PAGO"}
api.objetos.call_get_payment_getstatus(
    parameters=genera_parametros(parametros, api.secretKey)
)
```

__Para ver una lista de operaciones disponibles__:
```bash
poetry run pyflow operaciones
```
o
```bash
(venv) pyflow operaciones
```



"""
import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

import fsutil
import yaml
from openapi3 import OpenAPI
from slugify import slugify

from .exceptions import ConfigException
import logging

logger = logging.getLogger(__name__)


@dataclass
class FlowAPI(object):
    """
    Objeto principal, puede ser instanciado o heredado.

    Implementa todos los métodos de ``dataclass``.

    Attributes:
        api_key: APIKey entregado por Flow
        secret_key: SecretKey entregado por Flow
        use_sandbox: True para usar `sandbox`
        fragments: Listado de strings con las operaciones a realizar
    """

    """ api_key: APIKey entregado por Flow """
    api_key: str = None
    """ secret_key: SecretKey entregado por Flow """
    secret_key: str = None
    """ use_sandbox: True para usar `sandbox` """
    use_sandbox: bool = False
    """ fragments: Listado de strings con las operaciones a realizar"""
    fragments: list = field(default_factory=list)

    _base_path: Any = Path(__file__).resolve().parent
    _openapi3: Optional[OpenAPI] = field(init=False)

    def __post_init__(self):
        """Variables de inicio"""

        if not self.api_key:
            self.api_key = os.getenv("PYFLOWCL_API_KEY", None)
        if not self.secret_key:
            self.secret_key = os.getenv("PYFLOWCL_API_SECRET", None)
        if not self.use_sandbox:
            val = os.getenv("PYFLOWCL_USE_SANDBOX", "False")
            self.use_sandbox = True if (val.lower() == "true") else False
            del val
        # if not self._yaml_file:
        #     self._yaml_file = os.getenv("PYFLOWCL_YAML_FILE", None)
        # if not self._fix_openapi:
        #     val = os.getenv("PYFLOWCL_FIX_OPENAPI", "True")
        #     self._fix_openapi = True if (val.lower() == "true") else False
        #     del val
        self._openapi3 = None

        self.init_api()

    def init_api(self) -> None:
        """
        Genera las validaciones y configuraciones necesarias para leer el
        archivo YAML con la especificacion.
        """
        self.check_config()
        # self.load_yaml_spec(self.flow_yaml_file)

        # Flow no agrega operationId dentro de las propiedades de cada endpoint
        # Se crea uno para cada endpoint usando ``slugify``
        # `fix_it=False` para deshabilitar (por defecto en True)

        # self.create_openapi3()

    def check_config(self) -> bool:
        """
        Verifica que los datos de configuracion sean correctos.

        Se pueden definir desde la instancia

        ```python
        api = FlowAPI(api_key="APIKey", api_secret="SecretKey")
        ```
        o usando variables de entorno

        ```bash
        export PYFLOWCL_API_KEY="APIKey"
        export PYFLOWCL_API_SECRET="SecretKey"
        ```

        Returns:
            ``True`` si la validacion fue exitosa

        Raises:
            ConfigException: Cuando falta un parametro por definir
        """

        if self.use_sandbox and self._yaml_file:
            raise ConfigException(
                "No se puede definir `use_sandbox` y `_yaml_file`"
            )

        if not self.api_key:
            error_msg = 'Se necesita configurar FLOW_KEY, puedes agregarlo al constructor: api = FlowAPI(key="secret_key") o como variable de entorno: export PYFLOWCL_KEY="secret_key" '
            raise ConfigException(error_msg)

        if not self.secret_key:
            error_msg = 'Se necesita configurar FLOW_SECRET, puedes agregarlo al constructor api = FlowAPI(secret="secret") o como variable de entorno export PYFLOWCL_SECRET="secret" '
            raise ConfigException(error_msg)

        return True

    def load_yaml_spec(self, spec: str = None) -> None:
        if not spec:
            raise Exception("spec debe ser un documento/archivo YAML válido")
        try:
            self.flow_yaml_spec = load_yaml_file(spec)
        except OSError as e:
            raise e

    def create_openapi3(self, fix_it: bool = True) -> None:
        if fix_it:
            self.fix_openapi3()
        api_spec = OpenAPI(self.flow_yaml_spec)
        self._openapi3 = api_spec

    def fix_openapi3(self):
        """
        Por defecto, Flow no entrega "operationId" en cada una de las
        operaciones esto provoca que no sea posible generar llamadas
        automaticas.
        Este método crea el valor "operationId" y lo actualiza directamente en
        ``FlowAPI.flow_yaml_spec``.
        El valor de cada operacion es generado con slugify siguiendo esta
        estructura

        Examples:
            >>> slugify("get /payment/getStatus", separator="_")
            'get_payment_getstatus'
        """
        for path in self.flow_yaml_spec["paths"]:
            for verb in self.flow_yaml_spec["paths"][path]:
                slug = None
                # Saltar si existe
                if (
                    "operationId"
                    not in self.flow_yaml_spec["paths"][path][verb]
                ):
                    slug = slugify(f"{verb} {path}", separator="_")
                    self.flow_yaml_spec["paths"][path][verb][
                        "operationId"
                    ] = slug

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


with open("pyflowcl/fragments/fragment-core.yml") as f:
    core = yaml.safe_load(f.read())


with open("pyflowcl/fragments/fragment-sandbox-server.yml") as f:
    server = yaml.safe_load(f.read())

with open("pyflowcl/fragments/fragment-payments.yml") as f:
    payments = yaml.safe_load(f.read())
