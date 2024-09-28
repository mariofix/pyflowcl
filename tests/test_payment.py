from unittest.mock import MagicMock, patch

import pytest

from pyflowcl.Clients import ApiClient
from pyflowcl.models import GenericError, PaymentList, PaymentResponse, PaymentStatus
from pyflowcl.Payment import (
    create,
    createEmail,
    getPayments,
    getStatus,
    getStatusByCommerceId,
    getStatusByFlowOrder,
)


@pytest.fixture
def api_client():
    return ApiClient(api_key="test_key", api_secret="test_secret")


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatus(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "approved"}
    mock_get.return_value = mock_response

    result = getStatus(api_client, "test_token")
    assert isinstance(result, PaymentStatus)
    assert result.status == "approved"


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatusByCommerceId(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "pending"}
    mock_get.return_value = mock_response

    result = getStatusByCommerceId(api_client, "test_commerce_id")
    assert isinstance(result, PaymentStatus)
    assert result.status == "pending"


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatusByFlowOrder(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"status": "rejected"}
    mock_get.return_value = mock_response

    result = getStatusByFlowOrder(api_client, 12345)
    assert isinstance(result, PaymentStatus)
    assert result.status == "rejected"


@patch("pyflowcl.Clients.ApiClient.get")
def test_getPayments(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"total": 2, "hasMore": False, "data": [{"id": 1}, {"id": 2}]}
    mock_get.return_value = mock_response

    result = getPayments(api_client, {"start": "2023-01-01", "end": "2023-01-31"})
    assert isinstance(result, PaymentList)
    assert result.total == 2
    assert len(result.data) == 2


@patch("pyflowcl.Clients.ApiClient.post")
def test_create(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"url": "https://www.flow.cl/pay", "token": "test_token"}
    mock_post.return_value = mock_response

    payment_data = {
        "commerceOrder": "OC-123",
        "subject": "Test Payment",
        "amount": 1000,
        "email": "test@example.com",
        "urlConfirmation": "https://example.com/confirm",
        "urlReturn": "https://example.com/return",
    }
    result = create(api_client, payment_data)
    assert isinstance(result, PaymentResponse)
    assert result.url == "https://www.flow.cl/pay"
    assert result.token == "test_token"


@patch("pyflowcl.Clients.ApiClient.post")
def test_createEmail(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"url": "https://www.flow.cl/pay", "token": "test_token"}
    mock_post.return_value = mock_response

    payment_data = {
        "commerceOrder": "OC-123",
        "subject": "Test Payment",
        "amount": 1000,
        "email": "test@example.com",
        "urlConfirmation": "https://example.com/confirm",
        "urlReturn": "https://example.com/return",
        "messageBody": "Test payment message",
    }
    result = createEmail(api_client, payment_data)
    assert isinstance(result, PaymentResponse)
    assert result.url == "https://www.flow.cl/pay"
    assert result.token == "test_token"


@patch("pyflowcl.Clients.ApiClient.get")
def test_error_handling(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.json.return_value = {"code": "ERROR_CODE", "message": "Error message"}
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "test_token")

    assert exc_info.value.code == "ERROR_CODE"
    assert exc_info.value.message == "Error message"
