import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, Union
from warnings import warn

import fsutil
import yaml
from openapi3 import OpenAPI
from slugify import slugify


@dataclass
class FlowAPI:
    api_key: Union[None, str] = None
    api_secret: Union[None, str] = None
    endpoint: Union[None, str] = None
    _base_path: Any = Path(__file__).resolve().parent
    _yaml_file: Union[None, str] = None
    _openapi3: Union[None, OpenAPI] = field(init=False)

    def __post_init__(self):
        warn(
            """
            Lamentablemente el proyecto OpenAPI3 que era la base de este proyecto ha sido
            abandonado por su mantenedor, he decidio deprecar esta version y volver a la clase
            estable de este proyecto. Por favor mira la documentacion sobre como proseguir.
            """
        )
        if not self.api_key:
            self.api_key = os.getenv("PYFLOWCL_API_KEY", None)
        if not self.api_secret:
            self.api_secret = os.getenv("PYFLOWCL_API_SECRET", None)
        if not self.endpoint:
            self.endpoint = os.getenv("PYFLOWCL_ENDPOINT", "live")

        try:
            yaml_spec = load_yaml_file(f"{self._base_path}/yaml_files/apiFlow.{self.endpoint}.min.yaml")
        except Exception as e:
            raise Exception(f"No se pudo cargar el archivo: {e}")
        else:
            yaml_spec = self.fix_openapi3(yaml_spec)
            self._openapi3 = OpenAPI(yaml_spec)

    def fix_openapi3(self, flow_yaml_spec):
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
        return self._openapi3

    @property
    def operaciones(self) -> list:
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
