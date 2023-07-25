import pytest  # noqa: F401

from pyflowcl import FlowAPI, __version__, exceptions  # noqa: F401


def test_version():
    assert __version__ == "1.2.1"


def test_FlowAPI_min_config():
    api = FlowAPI(api_key="api-key", api_secret="secret-key")

    assert api.api_key == "api-key"
    assert api.api_secret == "secret-key"
    assert api.endpoint == "live"


# def test_FlowAPI_min_config_error():
#     with pytest.raises(exceptions.ConfigException):
#         FlowAPI()


# def test_FlowAPI_config_via_init_live():
#     api = FlowAPI(flow_key="api-key", flow_secret="secret-key")

#     assert api.flow_key == "api-key"
#     assert api.flow_secret == "secret-key"
#     assert api.flow_yaml_file.endswith("apiFlow.min.yaml")
#     assert api._openapi3 is not None


# def test_FlowAPI_config_via_init_no_fix():
#     api = FlowAPI(
#         flow_key="api-key", flow_secret="secret-key", fix_openapi=False
#     )

#     assert api.flow_key == "api-key"
#     assert api.flow_secret == "secret-key"
#     assert api.flow_yaml_file.endswith("apiFlow.min.yaml")
#     assert api._openapi3 is not None


# def test_FlowAPI_config_via_init_with_file():
#     api = FlowAPI(flow_key="api-key", flow_secret="secret-key")

#     assert api.flow_key == "api-key"
#     assert api.flow_secret == "secret-key"
#     assert api.flow_yaml_file.endswith("apiFlow.min.yaml")
#     assert api._openapi3 is not None


# def test_FlowAPI_config_via_init_wrongkeys():
#     api = FlowAPI(flow_key="api-key", flow_secret="secret-key")

#     assert api.flow_key != "different-key"
#     assert api.flow_secret != "different-secret"
#     assert api.flow_yaml_file != "different-file"


# def test_FlowAPI_configexception_key():
#     with pytest.raises(exceptions.ConfigException) as exc_info:
#         api = FlowAPI()


# def test_FlowAPI_configexception_secret():
#     with pytest.raises(exceptions.ConfigException) as exc_info:
#         api = FlowAPI(flow_key="key")


# def test_FlowAPI_configexception_env():
#     with pytest.raises(exceptions.ConfigException) as exc_info:
#         api = FlowAPI(flow_use_sandbox=True, flow_yaml_file="any-file")
