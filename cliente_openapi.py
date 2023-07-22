from pyflowcl import FlowAPI

# from pyflowcl.utils import genera_parametros

operaciones = FlowAPI().operaciones
print(f"{operaciones}")

# parametros = {"apiKey": api.apiKey, "token": "TOKEN"}
# print(api.objetos.call_get_payment_getstatus(parameters=genera_parametros(parametros, api.secretKey)))
