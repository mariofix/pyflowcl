# pyflowcl/__init__.py

"""
pyFlow Chile

La clase FlowAPI permite, con mínima codificacion, hacer llamadas a la API
de Flow Chile conociendo solamente la accion a realizar, sin configuraciones
ni validaciones tediosas.

Modulos disponibles:
- `FlowAPI` - API de trabajo con Flow.cl
- `ApiClient` -  Cliente API genérico, permite llamadas HTTP con validacion
X-Header-Token, deprecado.
"""

import logging

from .Clients import ApiClient
from .openapi3 import FlowAPI

__version__ = "1.1.2"

logger = logging.getLogger(__name__)
__all__ = ["FlowAPI", "ApiClient", "__version__", "logger"]
