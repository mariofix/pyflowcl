from typing import Any, Dict
from pyflowcl import Payment, Customer
from pyflowcl.Clients import ApiClient
import logging

logging.basicConfig(level=logging.DEBUG)

API_URL = "https://sandbox.flow.cl/api"
API_KEY = "5C627F95-4523-4AEB-9FBC-7883B1FL43E5"
API_SECRET = "43559f1ae777c3f4ff86fb752917356ebf6f2644"

api = ApiClient(API_URL, API_KEY, API_SECRET)
cust_data: Dict[str, Any] = {
    "start": 0
}

llamada = Customer.register(api, 4, "https://mariofix.com")
print(llamada)
"""
llamada = Customer.edit(api, cust_data)
print(llamada)

llamada = Customer.get(api, "cus_asg7nznrfp")
print(llamada)

llamada = Customer.get(api, "cus_kpiq2nvif0")
print(llamada)
"""

"""
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
"""