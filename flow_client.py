from typing import Any

from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

API_URL = "https://sandbox.flow.cl/api"
API_KEY = "5C627F95-4523-4AEB-9FBC-7883B1FL43E5"
API_SECRET = "c08a5046b3bc357bf1cd3db9286e7560b4451501"

api = ApiClient(
    api_url=API_URL,
    api_key=API_KEY,
    api_secret=API_SECRET,
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
