# API de Conexion para Flow.cl

Cliente API para operaciones con el servicio de pagos Flow.cl  [FlowAPI-3.0.1](https://www.flow.cl/docs/api.html)
Frunciona como wrapper sobre cliente [OpenAPI3](https://github.com/Dorthu/openapi3)


## Instalación
Este proyecto está desarrollado para Python 3.8 y superior.
Este proyecto es administrado por Poetry.

=== "Usando Poetry"
    ```shell
    poetry add pyflowcl
    ```
=== "Usando pip"
    ```shell
    pip install pyflowcl
    ```

## Uso
`flow_key` y `flow_secret` pueden ser configurados de dos maneras

=== "Constructor"
    ```python
    from pyflowcl import FlowAPI
    flow = FlowAPI(flow_key="key", flow_secret="secret")
    ```

=== "Variables de Entorno"
    ```shell
    export PYFLOWCL_KEY="key"
    export PYFLOWCL_SECRET="SECRET"
    python cliente_flow.py
    ```

## Siguientes pasos

Puedes revisar la [guia de uso](uso.md) o las [opciones avanzadas](uso-avanzado.md) para obtener mas información.
