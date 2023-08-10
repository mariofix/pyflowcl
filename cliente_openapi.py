from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

# Descomenta todo esto para habilitar debug logs en este ejemplo
#
# import http.client as http_client
# import logging
# http_client.HTTPConnection.debuglevel = 1
# logging.basicConfig()
# logging.getLogger().setLevel(logging.DEBUG)
# requests_log = logging.getLogger("requests.packages.urllib3")
# requests_log.setLevel(logging.DEBUG)
# requests_log.propagate = True

api = FlowAPI(
    api_key="FLOW API LKEY",
    api_secret="FLOW API SECRET",
    endpoint="sandbox",
)
parametros = {
    "apiKey": api.api_key,
    "amount": 10000,
    "currency": "CLP",
    "subject": "Pago desde pyFlowcl",
    "email": "mariofix@proton.me",
    "urlConfirmation": "https://mariofix.github.io/pyflowcl/uso/#crear-un-pago",
    "urlReturn": "https://mariofix.github.io/pyflowcl/uso/#crear-un-pago",
    "commerceOrder": "order_1234",
}
print("Creando Pago de Ejemplo...")
pago = api.objetos.call_payment_create(data=genera_parametros(parametros, api.api_secret))
print("Informacion de pago:")
print(pago)
parametros_status = {
    "apiKey": api.api_key,
    "token": pago.token,
}
print("Obteniendo Estado...")
estado = api.objetos.call_payment_getstatus(parameters=genera_parametros(parametros_status, api.api_secret))
print("Informacion de Estado:")
print(estado)
