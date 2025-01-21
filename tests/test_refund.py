from unittest.mock import MagicMock, patch

import pytest

from pyflowcl.Clients import ApiClient
from pyflowcl.models import GenericError, RefundStatus
from pyflowcl.Refund import create, getStatus


@pytest.fixture
def api_client():
    return ApiClient(api_key="test_key", api_secret="test_secret")


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowRefundOrder": 1234567,
        "requestDate": "2023-06-01",
        "amount": 1000,
        "status": 1,
        "token": "TEST_TOKEN",
    }
    mock_post.return_value = mock_response

    refund_data = {
        "flowRefundOrder": 1234567,
        "amount": 1000,
    }

    result = create(api_client, refund_data)

    assert isinstance(result, RefundStatus)
    assert result.flowRefundOrder == 1234567
    assert result.amount == 1000
    assert result.status == 1


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund_error(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"code": "ERROR_CODE", "message": "Error message"}
    mock_post.return_value = mock_response

    refund_data = {
        "flowOrder": 1234567,
        "commerceOrder": "OC-123",
        "amount": 1000,
        "receiverEmail": "test@example.com",
        "urlCallback": "https://example.com/callback",
    }

    with pytest.raises(GenericError) as exc_info:
        create(api_client, refund_data)

    assert exc_info.value.code == 400


@patch("pyflowcl.Clients.ApiClient.get")
def test_get_refund_status(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowRefundOrder": 1234567,
        "amount": 1000,
        "status": 2,
    }
    mock_get.return_value = mock_response

    result = getStatus(api_client, "TEST_TOKEN")

    assert isinstance(result, RefundStatus)
    assert result.flowRefundOrder == 1234567
    assert result.amount == 1000
    assert result.status == 2


@patch("pyflowcl.Clients.ApiClient.get")
def test_get_refund_status_error(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.json.return_value = {"code": "UNAUTHORIZED", "message": "Unauthorized access"}
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "TEST_TOKEN")

    assert exc_info.value.code == 401


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund_unexpected_error(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_post.return_value = mock_response

    refund_data = {
        "flowOrder": 1234567,
        "commerceOrder": "OC-123",
        "amount": 1000,
        "receiverEmail": "test@example.com",
        "urlCallback": "https://example.com/callback",
    }

    with pytest.raises(GenericError) as exc_info:
        create(api_client, refund_data)

    assert exc_info.value.code == 500
    assert isinstance(exc_info.value.message, MagicMock)


@patch("pyflowcl.Clients.ApiClient.get")
def test_get_refund_status_unexpected_error(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "TEST_TOKEN")

    assert exc_info.value.code == 500
    assert isinstance(exc_info.value.message, MagicMock)
