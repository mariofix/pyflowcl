from typing import Any, Dict
from pyflowcl import Payment
from pyflowcl.Clients import ApiClient
import logging

logging.basicConfig(level=logging.DEBUG)

API_URL = "https://sandbox.flow.cl/api"
API_KEY = "your_key"
API_SECRET = "your_secret"

api = ApiClient(API_URL, API_KEY, API_SECRET)

pago: Dict[str, Any] = {
    "subject": "Asunto Email",
    "commerceOrder": "1234",
    "amount": 5000,
    "email": "mariofix@pm.me",
    "urlConfirmation": "https://mariofix.com",
    "urlReturn": "https://mariofix.com",
}
llamada = Payment.create(api, pago)
print(llamada)
del llamada

llamada = Payment.createEmail(api, pago)
print(llamada)
del llamada

llamada = Payment.getStatus(api, "token")
print(llamada)
del llamada

llamada = Payment.getStatusByCommerceId(api, "commerce-id")
print(llamada)
del llamada

llamada = Payment.getStatusByFlowOrder(api, "flow-order")
print(llamada)
del llamada

data: Dict[str, Any] = {"apiKey": "", "date": "yyyy-mm-dd"}
llamada = Payment.getPayments(api, data)
print(llamada)
del llamada
