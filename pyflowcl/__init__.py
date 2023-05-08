# pyflowcl/__init__.py

"""
Entrega funciones de procesamiento de la API de Flow Chile para procesamiento de pagos.  

La clase FlowAPI permite, con mínima codificacion, hacer llamadas a la API de Flow Chile
conociendo solamente la accion a realizar, sin configuraciones ni validaciones tediosas.  

Modulos disponibles:  
- `FlowAPI` - Wrapper sobre OpenAPI3, permite descubrir los métodos y funciones usando 
el archivo openapi directamente.  
- `ApiClient` -  Cliente API genérico, permite llamadas HTTP con validacion
X-Header-Token  

"""

### TODO: Setear Logger
from .openapi3 import FlowAPI
from .Clients import ApiClient

__version__ = "1.1.2"


__all__ = ["FlowAPI", "ApiClient", "__version__"]
