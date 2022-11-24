from dataclasses import dataclass, field
from openapi3 import OpenAPI
import yaml
import os

__version__ = "1.1.0"


@dataclass
class FlowAPI(object):
    _openapi3: OpenAPI = field(init=False)
    flow_key: str = None
    flow_secret: str = None

    def __post_init__(self):
        if not self.flow_key:
            self.flow_key = os.getenv("PYFLOWCL_KEY", None)
        if not self.flow_secret:
            self.flow_secret = os.getenv("PYFLOWCL_SECRET", None)
        self._openapi3 = None

        self.check_config()

    def check_config(self):
        if not self.flow_key:
            raise Exception(
                'Se necesita configurar FLOW_KEY, puedes agregarlo al constructor api = FlowAPI(key="secret_key") o como variable de entorno export PYFLOWCL_KEY="secret_key" '
            )
        if not self.flow_secret:
            raise Exception(
                'Se necesita configurar FLOW_SECRET, puedes agregarlo al constructor api = FlowAPI(secret="secret") o como variable de entorno export PYFLOWCL_SECRET="secret" '
            )
