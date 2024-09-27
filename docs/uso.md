# Cómo Usar la API de Flow

Este ejemplo muestra cómo realizar diversas operaciones usando la API de Flow para pagos en Chile.

## Requisitos

Antes de comenzar, asegúrate de tener las siguientes cosas configuradas:

- Una cuenta activa en Flow.cl
- Tu `ApiKey` y `ApiSecret` proporcionados por Flow
- Python 3.9 o superior

## Configuración

Define las credenciales de tu API y la URL base de la API de Flow. Estas deben ser proporcionadas por Flow cuando configures tu cuenta:

```python
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)
```

## Crear un Pago

Para crear un pago, debes definir los detalles del mismo en un diccionario. Aquí tienes un ejemplo:

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
```

## Enviar Pago por Email

Puedes enviar un pago por correo electrónico utilizando el siguiente código:

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

llamada = Payment.createEmail(api, pago)
print(f"{llamada = }")
```

## Consultar Estado del Pago

Para verificar el estado de un pago, puedes utilizar el token del pago, el ID de comercio o el número de orden de Flow.

### Estado por Token

```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)

llamada = Payment.getStatus(api, "token")
print(f"{llamada = }")
```

### Estado por ID de Comercio

```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)

llamada = Payment.getStatusByCommerceId(api, "commerce-id")
print(f"{llamada = }")
```

### Estado por Número de Orden de Flow

```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)

llamada = Payment.getStatusByFlowOrder(api, "flow-order")
print(f"{llamada = }")
```

## Obtener Todos los Pagos

Para obtener una lista de pagos, utiliza las siguientes configuraciones:

```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url="https://www.flow.cl/api",
    api_key="tu_api_key",
    api_secret="tu_api_secret",
)

data = {"apiKey": "tu_api_key", "date": "yyyy-mm-dd"}
llamada = Payment.getPayments(api, data)
print(f"{llamada = }")
```

## Resumen

Este ejemplo cubre cómo configurar la API de Flow y realizar varias operaciones relacionadas con pagos. Asegúrate de tener tus credenciales correctas y de probar las funcionalidades antes de implementarlas en producción.
