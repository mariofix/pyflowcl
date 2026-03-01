import hashlib
import hmac
from unittest.mock import MagicMock, patch

import pytest
import requests

from pyflowcl.Clients import ApiClient
from pyflowcl.exceptions import ConfigException


def test_init_default_values():
    client = ApiClient()
    assert client.api_url == "https://www.flow.cl/api"
    assert client.api_key is None
    assert client.api_secret is None


def test_init_custom_values():
    client = ApiClient(api_url="https://custom.api.url", api_key="custom_key", api_secret="custom_secret")
    assert client.api_url == "https://custom.api.url"
    assert client.api_key == "custom_key"
    assert client.api_secret == "custom_secret"


def test_make_signature(api_client):
    params = {"apiKey": "test_key", "amount": 1000, "subject": "Test Payment", "empty": None}

    string = "apiKeytest_keyamount1000subjectTest Payment"
    expected_signature = hmac.new(b"test_secret", string.encode(), hashlib.sha256).hexdigest()

    assert api_client.make_signature(params) == expected_signature


def test_make_signature_empty_params(api_client):
    params = {}
    expected_signature = hmac.new(b"test_secret", b"", hashlib.sha256).hexdigest()

    assert api_client.make_signature(params) == expected_signature


def test_make_signature_raises_without_secret():
    client = ApiClient(api_key="test_key")
    with pytest.raises(ConfigException, match="api_secret is required"):
        client.make_signature({"apiKey": "test_key"})


def test_make_signature_with_special_chars(api_client):
    params = {"apiKey": "test_key", "subject": "Test & Payment", "description": "Payment for item #123"}

    signature = api_client.make_signature(params)
    assert len(signature) == 64  # SHA256 produces 64-char hex digest


@patch("pyflowcl.Clients.requests.get")
def test_get_request(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "success"}
    mock_get.return_value = mock_response

    url = "https://api.example.com/endpoint"
    query_params = {"param1": "value1", "param2": "value2"}

    response = api_client.get(url, query_params)

    mock_get.assert_called_once_with(url, params=query_params, timeout=5)
    assert response is mock_response


@patch("pyflowcl.Clients.requests.post")
def test_post_request(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.json.return_value = {"status": "success"}
    mock_post.return_value = mock_response

    url = "https://api.example.com/endpoint"
    post_data = {"field1": "value1", "field2": "value2"}

    response = api_client.post(url, post_data)

    mock_post.assert_called_once_with(url, data=post_data, timeout=5)
    assert response is mock_response


@patch("pyflowcl.Clients.requests.get")
def test_get_request_timeout(mock_get, api_client):
    mock_get.side_effect = requests.Timeout()

    with pytest.raises(requests.Timeout):
        api_client.get("https://api.example.com/endpoint", {})


@patch("pyflowcl.Clients.requests.post")
def test_post_request_timeout(mock_post, api_client):
    mock_post.side_effect = requests.Timeout()

    with pytest.raises(requests.Timeout):
        api_client.post("https://api.example.com/endpoint", {})
