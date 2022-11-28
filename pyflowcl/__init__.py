# pyflowcl/__init__.py

"""
Entrega funciones de procesamiento de la API de Flow Chile para procesamiento de pagos.  

La clase FlowAPI permite, con mínima codificacion, hacer llamadas a la API de Flow Chile
conociendo solamente la accion a realizar, sin configuraciones ni validaciones tediosas.  

Modulos disponibles:  
- `ApiClient`: Cliente API genérico, permite llamadas HTTP con validacion X-Header-Token  
- `FlowAPI`: Wrapper sobre OpenAPI3, permite descubrir los métodos y funciones usando 
el archivo openapi directamente.  

"""
from pyflowcl.flowapi_spec import FlowAPI
from pyflowcl.Clients import ApiClient

__version__ = "1.1.0"


# __all__ = ["FlowAPI", "ApiClient", "ConfigException", "__version__"]
