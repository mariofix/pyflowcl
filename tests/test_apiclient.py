from unittest.mock import MagicMock, patch

import pytest

from pyflowcl.Clients import ApiClient  # Asegúrate de importar ApiClient correctamente


@pytest.fixture
def api_client():
    return ApiClient(api_key="test_key", api_secret="test_secret")


def test_make_signature(api_client):
    params = {"param1": "value1", "param2": "value2"}
    signature = api_client.make_signature(params)
    assert isinstance(signature, str)
    assert len(signature) == 64  # SHA256 produce una firma de 64 caracteres en hexadecimal


def test_make_signature_with_none_values(api_client):
    params = {"param1": "value1", "param2": None, "param3": "value3"}
    signature = api_client.make_signature(params)
    assert isinstance(signature, str)
    assert len(signature) == 64


@patch("requests.get")
def test_get(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {"key": "value"}
    mock_get.return_value = mock_response

    url = "test_url"
    query_string = {"param": "value"}
    response = api_client.get(url, query_string)

    mock_get.assert_called_once_with(url, params=query_string)
    assert response.json() == {"key": "value"}


@patch("requests.post")
def test_post(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {"key": "value"}
    mock_post.return_value = mock_response

    url = "test_url"
    post_data = {"param": "value"}
    response = api_client.post(url, post_data)

    mock_post.assert_called_once_with(url, data=post_data)
    assert response.json() == {"key": "value"}


def test_api_client_initialization():
    client = ApiClient(api_key="custom_key", api_secret="custom_secret")
    assert client.api_key == "custom_key"
    assert client.api_secret == "custom_secret"
    assert client.api_url == "https://www.flow.cl/api"


def test_api_client_default_values():
    client = ApiClient()
    assert client.api_key == ""
    assert client.api_secret == ""
    assert client.api_url == "https://www.flow.cl/api"
