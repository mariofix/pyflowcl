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

## Uso Básico

Aquí hay un ejemplo básico de cómo usar pyflowcl para crear un pago:

```shell
from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(api_key="tu llave flow", api_secret="tu secreto flow")
parametros = {
    "apiKey": api.api_key,
    amount=10000,
    currency="CLP",
    subject="Ejemplo de Pago",
    email="correo@example.com",
    url_confirmation="https://mi-sitio.com/confirmacion",
    }
pago = api.objetos.call_payment_create(parameters=genera_parametros(parametros, api.api_secret))
print(pago)
> { "flowOrder": 123456, "url": "https://www.flow.cl/app/pay.php", "token": "tok_123456" }

# Obtiene la URL de pago
url_pago = pago.get("url")
token_pago = pago.get("url")
print(f"URL de pago: {url_pago}?token={token_pago}")
```

## Siguientes pasos

Puedes revisar la [guia de uso](uso.md) o las [opciones avanzadas](uso-avanzado.md) para obtener mas información.
