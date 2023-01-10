from pyflowcl import FlowAPI
from pyflowcl.utils import genera_parametros

api = FlowAPI(
    flow_key="APIKey",
    flow_secret="secretKey",
)
api.init_api()
parametros = {"apiKey": api.apiKey, "token": "TOKEN"}
print(
    api.objetos.call_get_payment_getstatus(
        parameters=genera_parametros(parametros, api.secretKey)
    )
)
