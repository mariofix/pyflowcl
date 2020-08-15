from dataclasses import asdict

from pyflowcl import Payment
from pyflowcl.Clients import ApiClient

api = ApiClient(
    "https://sandbox.flow.cl/api",
    "api_key",
    "api_secret",
)

llamada = Payment.get_status(api, "notification_token")
print(llamada)
del llamada

llamada = Payment.get_status_by_commerce_id(api, "commerce_id")
print(llamada)
del llamada

llamada = Payment.get_status_by_flow_order(api, 11111)
print(llamada)
del llamada