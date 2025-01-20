import os
from typing import Any

from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    api_url=os.getenv("API_URL"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET"),
)

pago = {
    "subject": "Asunto Email",
    "commerceOrder": "1234",
    "amount": 5000,
    "email": "mariofix@pm.me",
    "urlConfirmation": "https://mariofix.com",
    "urlReturn": "https://mariofix.com",
    "currency": "CLP",
}
llamada = Payment.create(api, pago)
print(f"{llamada = }")

llamada = Payment.createEmail(api, pago)
print(f"{llamada = }")

llamada = Payment.getStatus(api, "token")
print(f"{llamada = }")


llamada = Payment.getStatusByCommerceId(api, "commerce-id")
print(f"{llamada = }")


llamada = Payment.getStatusByFlowOrder(api, "flow-order")
print(f"{llamada = }")


data: dict[str, Any] = {"apiKey": "", "date": "yyyy-mm-dd"}
llamada = Payment.getPayments(api, data)
print(f"{llamada = }")
