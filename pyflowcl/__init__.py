# pyflowcl/__init__.py

"""
pyFlow Chile

La clase FlowAPI permite, con mínima codificacion, hacer llamadas a la API
de Flow Chile conociendo solamente la accion a realizar, sin configuraciones
ni validaciones tediosas.

Modulos disponibles:
- `FlowAPI` - API de trabajo con Flow.cl
"""

import logging

from .openapi3 import FlowAPI

__version__ = "1.1.4"

logger = logging.getLogger(__name__)
__all__ = ["FlowAPI", "__version__", "logger"]
