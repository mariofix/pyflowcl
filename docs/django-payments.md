# Integración de Django-Payments con Flow

Django-Payments es un sistema universal de manejo de pagos para Django. Este documento detalla los pasos para integrar Flow con Django-Payments utilizando la librería `pyflowcl`.

## Instalación

Existen dos métodos principales para instalar `django-payments-flow`:

### Usando Poetry

```shell
poetry add django-payments-flow
```

### Usando pip

```shell
pip install django-payments-flow
```

## Configuración Básica

Configura el proveedor de Flow en tu archivo `settings.py`:

```python
PAYMENT_VARIANTS = {
    "flow": ("django_payments_flow.FlowProvider", {
        "key": "ApiKey",
        "secret": "ApiSecret",
        "sandbox": True,  # Usar True para pruebas, False para producción
    })
}
```

Reemplaza `"ApiKey"` y `"ApiSecret"` con tus credenciales reales de Flow.

## Uso Básico

Ahora crea un pago usando el nombre de la variante correspondiente a Flow.

```python
from django_payments import get_payment_model

Payment = get_payment_model()
payment = Payment.objects.create(
    variant='flow',  # Debe coincidir con la clave en PAYMENT_VARIANTS
    description='Compra de producto XYZ',
    total=1000,
    currency='CLP',
    billing_first_name='Juan',
    billing_last_name='Pérez',
    billing_address_1='Calle Principal 123',
    billing_address_2='Depto 45',
    billing_city='Santiago',
    billing_postcode='8320000',
    billing_country_code='CL',
    billing_country_area='Región Metropolitana',
)
```

## Configuración Avanzada

Para opciones de configuración más avanzadas, consulta la [documentación oficial de django-payments-flow](https://mariofix.github.io/django-payments-flow/uso/#variables-de-configuracion).
