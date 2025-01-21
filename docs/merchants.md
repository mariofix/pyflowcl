# Integración de Merchants con Flow

Merchants es un sistema universal de manejo de pagos para Starlette/FastAPI. Este documento detalla los pasos para integrar Flow con Merchants utilizando la librería `pyflowcl`.

## Instalación

```shell
pip install merchants
```

## Configuración Básica

Configura la integracion de Flow en tu aplicacion:

```python
from merchants.app import merchants_config

merchants_config.add_integration(
    "flow-webpay",
    endpoint="merchants.integrations.FlowIntegration",
    config={
        "api_key": "ApiKey",
        "api_secret": "ApiSecret",
        "ambiente": "live",  # Usar sandbox para pruebas, live para producción
        "medio": 1,
    },
)
merchants_config.add_integration(
    "flow-servipag",
    endpoint="merchants.integrations.FlowIntegration",
    config={
        "api_key": "ApiKey",
        "api_secret": "ApiSecret",
        "ambiente": "live",  # Usar sandbox para pruebas, live para producción
        "medio": 3,
    },
)
```

Puedes crear distintas integraciones con los mismos datos para crear links con medios de pago específicos.

Reemplaza `"ApiKey"` y `"ApiSecret"` con tus credenciales reales de Flow.

## Uso Básico

TODO

## Configuración Avanzada

Para opciones de configuración más avanzadas, consulta la [documentación oficial de merchants](https://mariofix.github.io/merchants/).
