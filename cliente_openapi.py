import http.client as http_client
import logging

from rich import print

from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

http_client.HTTPConnection.debuglevel = 1

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

api = FlowAPI(
    api_key="5C627F95-4523-4AEB-9FBC-7883B1FL43E5",
    api_secret="43559f1ae777c3f4ff86fb752917356ebf6f2644",
    endpoint="sandbox",
)
print(f"{api.objetos.paths['/payment/create']=}")
# parametros = {
#     "apiKey": api.api_key,
#     "amount": 10000,
#     "currency": "CLP",
#     "subject": "Pago desde pyFlowcl con openapi3",
#     "email": "mariofix@proton.me",
#     "url_confirmation": "https://mariofix.github.io/pyflowcl/uso/#crear-un-pago",
# }
# pago = api.objetos.call_payment_create(data=genera_parametros(parametros, api.api_secret))
# print(pago)
