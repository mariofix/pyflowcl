from typing import Any
from dataclasses import dataclass, field
from openapi3 import OpenAPI
import yaml
import os
from pyflowcl.exceptions import ConfigException
from functools import lru_cache
import fsutil
import logging


@dataclass
class FlowAPI(object):
    _openapi3: Any = field(init=False)
    flow_key: str = None
    flow_secret: str = None
    flow_yaml_file: str = None
    flow_yaml_spec: str = field(repr=False, default=None)

    def __post_init__(self):
        if not self.flow_key:
            self.flow_key = os.getenv("PYFLOWCL_KEY", None)
        if not self.flow_secret:
            self.flow_secret = os.getenv("PYFLOWCL_SECRET", None)
        if not self.flow_yaml_file:
            self.flow_yaml_file = os.getenv("PYFLOWCL_YAML_FILE", None)
        self._openapi3 = None

    def init_api(self) -> None:
        self.check_config()
        self.set_yaml_file()
        self.load_yaml_spec(self.flow_yaml_file)
        return True

    def set_yaml_file(self) -> None:
        if not self.flow_yaml_file:
            # No se ingresó por constructor ni por env
            self.flow_yaml_file = fsutil.join_filepath(
                fsutil.get_parent_dir(__file__), "cache/apiFlow.yaml"
            )

    def check_config(self, raise_exceptions: bool = True) -> bool:
        if not self.flow_key:
            error_msg = 'Se necesita configurar FLOW_KEY, puedes agregarlo al constructor: api = FlowAPI(key="secret_key") o como variable de entorno: export PYFLOWCL_KEY="secret_key" '
            if raise_exceptions:
                raise ConfigException(error_msg)
            else:
                logging.error(error_msg)
                return False

        if not self.flow_secret:
            error_msg = 'Se necesita configurar FLOW_SECRET, puedes agregarlo al constructor api = FlowAPI(secret="secret") o como variable de entorno export PYFLOWCL_SECRET="secret" '
            if raise_exceptions:
                raise ConfigException(error_msg)
            else:
                logging.error(error_msg)
                return False

        return True

    def load_yaml_spec(self, spec: str = None, download: bool = True) -> None:
        if not spec:
            raise Exception("spec debe ser un documento/archivo YAML válido")
        try:
            self.flow_yaml_spec = load_yaml_file(spec)
        except OSError as e:
            if download:
                self.download_flow_spec()
            else:
                raise e

    def download_flow_spec(self) -> None:
        dest_folder = fsutil.join_filepath(fsutil.get_parent_dir(__file__), "cache")
        dest_file = "apiFlow.yaml"
        try:
            fsutil.download_file(
                url="https://www.flow.cl/docs/apiFlow.yaml?v=6",
                dirpath=dest_folder,
                filename=dest_file,
            )
            self.load_yaml_spec(
                fsutil.join_filepath(dest_folder, dest_file), download=False
            )
        except Exception as e:  # pragma nocover
            logging.error(e)
            raise e


@lru_cache()
def load_yaml_file(yaml_file: str = None) -> str:
    if not fsutil.is_file(yaml_file):
        raise OSError(f"El archivo {yaml_file} no existe.")

    with open(yaml_file) as f:
        """
        Se eliminan \\t ya que el archivo de flow tiene un error de formato
        """
        return yaml.safe_load(f.read().replace("\t", ""))
