# pyFlowCL

Cliente API para operaciones con el servicio de pagos Flow.cl  [FlowAPI-3.0.1](https://www.flow.cl/docs/api.html)  
Frunciona como wrapper sobre cliente [OpenAPI3] (https://github.com/Dorthu/openapi3)  


## Instalación
Este proyecto está desarrollado para Python 3.7 y superior.  
Este proyecto es administrado por Poetry.  


```bash
# con Poetry
$ poetry add pyflowcl
# con PIP
$ pip install pyflowcl
```


## Uso
APIKey y SecretKey pueden ser configurados de dos maneras

### Usando el constructor
```python
from pyflowcl import FlowAPI

flow = FlowAPI(flow_key="key", flow_secret="secret")
```

### Usando variables de entorno

```bash
export PYFLOWCL_KEY="key"
export PYFLOWCL_SECRET="SECRET"
python cliente_flow.py
```


## Resumen

::: pyflowcl