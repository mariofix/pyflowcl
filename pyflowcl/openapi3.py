import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Union

import fsutil
import yaml
from openapi3 import OpenAPI
from slugify import slugify


@dataclass
class FlowAPI:
    """
    Clase para interactuar con la API de Flow.

    Args:
        api_key (str, optional): Clave de API para autenticación. Si no se proporciona, se tomará del entorno.
        api_secret (str, optional): Secreto de API para autenticación. Si no se proporciona, se tomará del entorno.
        endpoint (str, optional): Ambiente Flow para llamadas ("live" o "sandbox").
    """

    api_key: Union[None, str] = None
    api_secret: Union[None, str] = None
    endpoint: str = "live"
    _base_path: Any = Path(__file__).resolve().parent
    _yaml_file: Union[None, str] = None
    _openapi3: Union[None, OpenAPI] = field(init=False)

    def __post_init__(self):
        if not self.api_key:
            self.api_key = os.getenv("PYFLOWCL_API_KEY", None)
        if not self.api_secret:
            self.api_secret = os.getenv("PYFLOWCL_API_SECRET", None)
        if not self.endpoint:
            self.endpoint = os.getenv("PYFLOWCL_ENDPOINT", "live")

        try:
            yaml_spec = load_yaml_file(f"{self._base_path}/yaml_files/apiFlow.min.yaml")
        except Exception as e:
            raise Exception(f"No se pudo cargar el archivo: {e}")
        else:
            yaml_spec = self.fix_openapi3(yaml_spec)
            self._openapi3 = OpenAPI(yaml_spec)

    def fix_openapi3(self, flow_yaml_spec):
        """
        Por defecto, Flow no entrega "operationId" en cada una de las
        operaciones esto provoca que no sea posible generar llamadas
        automaticas.
        Este método crea el valor "operationId" y lo actualiza directamente en
        ``self._openapi3``.
        El valor de cada operacion es generado con slugify siguiendo esta
        estructura

        Examples:
            >>> slugify(f"{path}", separator="_")
            'payment_getstatus'
        """
        for path in flow_yaml_spec["paths"]:
            for verb in flow_yaml_spec["paths"][path]:
                slug = None
                # Saltar si existe
                if "operationId" not in flow_yaml_spec["paths"][path][verb]:
                    slug = slugify(f"{path}", separator="_")
                    flow_yaml_spec["paths"][path][verb]["operationId"] = slug

        return flow_yaml_spec

    @property
    def objetos(self) -> OpenAPI:
        """
        Propiedad que devuelve el objeto OpenAPI de la API de Flow.

        Returns:
            OpenAPI: El objeto OpenAPI que contiene la especificación de la API de Flow.
        """
        return self._openapi3

    @property
    def operaciones(self) -> list:
        """
        Propiedad que devuelve una lista de las operaciones disponibles en la API de Flow.

        Returns:
            list: Lista de las operaciones disponibles en la API de Flow.
        """
        return list(self._openapi3._operation_map)


@lru_cache
def load_yaml_file(yaml_file: str = None) -> Any:
    """
    Carga un archivo YAML y devuelve su contenido.

    Args:
        yaml_file (str, optional): Ruta al archivo YAML. Default es None.

    Returns:
        Any: Contenido del archivo YAML.
    """
    if not fsutil.is_file(yaml_file):
        raise OSError(f"El archivo {yaml_file} no existe.")

    with open(yaml_file) as f:
        """Se eliminan ``\\t`` ya que el archivo de flow tiene un error de formato"""
        return yaml.safe_load(f.read().replace("\t", ""))
