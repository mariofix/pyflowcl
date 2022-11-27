from pyflowcl import __version__, FlowAPI, exceptions
import pytest
import fsutil


def test_version():
    assert __version__ == "1.1.0"


def test_FlowAPI_base():
    api = FlowAPI()

    assert hasattr(api, "_openapi3") is True
    assert hasattr(api, "flow_key") is True
    assert hasattr(api, "flow_secret") is True
    assert hasattr(api, "flow_yaml_file") is True
    assert hasattr(api, "flow_yaml_spec") is True


def test_FlowAPI_config_via_init():
    api = FlowAPI(
        flow_key="api-key", flow_secret="secret-key", flow_yaml_file="file.yaml"
    )

    assert api.flow_key == "api-key"
    assert api.flow_secret == "secret-key"
    assert api.flow_yaml_file == "file.yaml"
    assert api._openapi3 is None


def test_FlowAPI_config_via_init_wrongkeys():
    api = FlowAPI(
        flow_key="api-key", flow_secret="secret-key", flow_yaml_file="file.yaml"
    )

    assert api.flow_key != "different-key"
    assert api.flow_secret != "different-secret"
    assert api.flow_yaml_file != "different-file"
    assert api._openapi3 is None


def test_FlowAPI_config_via_attrs():
    api = FlowAPI()
    api.flow_key = "api-key"
    api.flow_secret = "secret-key"
    api.flow_yaml_file = "file.yaml"
    assert api.flow_key == "api-key"
    assert api.flow_secret == "secret-key"
    assert api.flow_yaml_file == "file.yaml"
    assert api._openapi3 is None


def test_FlowAPI_configexception_key():
    api = FlowAPI()
    with pytest.raises(exceptions.ConfigException) as exc_info:
        api.check_config()


def test_FlowAPI_configexception_secret():
    api = FlowAPI(flow_key="key")
    with pytest.raises(exceptions.ConfigException) as exc_info:
        api.check_config()


def test_FlowAPI_configerror_key():
    api = FlowAPI()
    assert api.check_config(raise_exceptions=False) is False


def test_FlowAPI_configerror_secret():
    api = FlowAPI(flow_key="key")
    assert api.check_config(raise_exceptions=False) is False


def test_FlowAPI_check_config():
    api = FlowAPI(flow_key="key", flow_secret="secret")
    assert api.check_config(raise_exceptions=False) is True


def test_FlowAPI_set_yaml_file():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    assert api.flow_yaml_file is None
    api.set_yaml_file()
    assert api.flow_yaml_file.endswith("cache/apiFlow.yaml")


def test_FlowAPI_load_yaml_spec():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    api.set_yaml_file()
    api.load_yaml_spec(api.flow_yaml_file)
    assert api.flow_yaml_spec is not None


def test_FlowAPI_load_yaml_no_spec_no_download():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    with pytest.raises(Exception) as exc_info:
        api.load_yaml_spec(None, download=False)


def test_FlowAPI_load_yaml_spec_file_not_found_no_download():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    api.flow_yaml_file = "nofile.bleh"
    with pytest.raises(OSError) as exc_info:
        api.load_yaml_spec(api.flow_yaml_file, download=False)


def test_FlowAPI_load_yaml_no_spec_download():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    with pytest.raises(Exception) as exc_info:
        api.load_yaml_spec(None)


def test_FlowAPI_load_yaml_spec_file_not_found_download():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    api.flow_yaml_file = "nofile.bleh"
    api.load_yaml_spec(api.flow_yaml_file) is True


def test_FlowAPI_init_api():
    api = FlowAPI(flow_key="api-key", flow_secret="secret-key")
    assert api.init_api() is True
