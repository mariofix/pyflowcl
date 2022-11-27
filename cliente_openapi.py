from pyflowcl import FlowAPI

# api = OpenAPI(spec)
# api.servers[0].url  - produccion
# api.servers[1].url  - sandbox

# api.paths['/payment/getStatus'].[get,post,put].request(api.servers[1].url).[body,headers,etc]

api = FlowAPI(flow_key="key", flow_secret="secret")
api.init_api()
# print(f"{api=}")
