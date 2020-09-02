PyFlowCL
============

Cliente API para operaciones con el servicio de pagos Flow.cl  
[FlowAPI-3.0.1](https://www.flow.cl/docs/api.html) 

---

## Comandos Habilitados
- [Payment](https://www.flow.cl/docs/api.html#tag/payment)
- [Refund](https://www.flow.cl/docs/api.html#tag/refund)


---

## Instalacion
Este proyecto es administrado por Poetry.  
Se entrega archivo requirements.txt


---

## Uso
```python
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

API_URL = "https://sandbox.flow.cl/api"
API_KEY = "your_key"
API_SECRET = "your_secret"
FLOW_TOKEN = "your_payment_token"
api = ApiClient(API_URL, API_KEY, API_SECRET)

call = Payment.getStatus(api, FLOW_TOKEN)
print(call)
```

---

## Licencia
>Puedes revisar el texto completo de la licencia [aqui](https://github.com/mariofix/pyflowcl/blob/stable-v3/LICENSE)

Este proyecto está licenciado bajo los términos de la licencia **MIT**.  
FlowAPI está licenciado bajo los términos de la licencia **Apache 2.0**.
