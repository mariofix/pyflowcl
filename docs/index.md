# API de Conexion para Flow.cl

pyflowcl es una biblioteca de Python que proporciona una interfaz para interactuar con la API de Flow en Chile. Con pyflowcl, puedes realizar diversas operaciones, como crear pagos, obtener información de pagos, realizar reembolsos y más.

## Instalación

Este proyecto está desarrollado para Python 3.9 y superior.
Este proyecto es administrado por Poetry.

=== "Usando Poetry"
`shell
    poetry add pyflowcl
    `
=== "Usando pip"
`shell
    pip install pyflowcl
    `

## Uso Básico

Aquí hay un ejemplo básico de cómo usar pyflowcl para crear un pago:

```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)
pago = {
    "subject": "Asunto Email",
    "commerceOrder": "1234",
    "amount": 5000,
    "email": "mariofix@pm.me",
    "urlConfirmation": "https://mariofix.com",
    "urlReturn": "https://mariofix.com",
}

llamada = Payment.create(api, pago)
print(f"{llamada = }")
> llamada = { "flowOrder": 123456, "url": "https://www.flow.cl/app/pay.php", "token": "tok_123456" }

# Obtiene la URL de pago
print(f"URL de pago: {pago.url}?token={pago.token}")
> URL de pago: https://www.flow.cl/app/pay.php?token=tok_123456
```

## Siguientes pasos

Puedes revisar la [guia de uso](uso.md) o las integraciones con [Django Payments](django-payments.md) o [Merchants](merchants.md) para obtener mas información.

## ¿Por que el cambio?

**TL;DR**: Por la falta de mantencion en openapi3 he decidido deprecar su soporte.

Hace aproximadamente 10 años comencé a desarrollar esta librería con el objetivo de crear una herramienta simple y funcional para el sistema en el que estaba trabajando. Aunque el primer commit es de hace 4 años, la he estado utilizando desde entonces, refinándola según las necesidades. Inicialmente, implementé el manejo de pagos y reembolsos, y en ese momento, funcionaba perfectamente. Sin embargo, cuando intenté añadir soporte para suscripciones y otras características más complejas, me encontré con que la API era mucho más extensa de lo que esperaba. Además, surgió un problema de formato en el archivo que impidió que se pudiera leer correctamente.

Investigando soluciones, descubrí la librería Dorthu/openapi3, que permitía generar automáticamente una API a partir del archivo YAML proporcionado por Flow, lo que parecía ideal para simplificar el proceso en Python. Implementé el soporte completo para la API, logrando que funcionara en un 90%, aunque todavía no es completamente usable. Intenté contribuir con una solución para un bug, pero no fue aceptada. Además, el mantenedor no ha realizado actualizaciones en los últimos dos años. Por eso, he decidido dejar de dar soporte a FlowAPI y migrar hacia FlowClient, actualizando la documentación en consecuencia. Los pasos para realizar esta transición están detallados en la documentación.
