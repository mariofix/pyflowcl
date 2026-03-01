from unittest.mock import MagicMock, patch

import pytest

from pyflowcl.models import GenericError, PaymentList, PaymentResponse, PaymentStatus
from pyflowcl.Payment import (
    create,
    createEmail,
    getPayments,
    getStatus,
    getStatusByCommerceId,
    getStatusByFlowOrder,
)


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatus(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowOrder": 1001,
        "commerceOrder": "OC-001",
        "status": 1,
        "amount": 5000.0,
        "payer": "payer@example.com",
    }
    mock_get.return_value = mock_response

    result = getStatus(api_client, "test_token")

    assert isinstance(result, PaymentStatus)
    assert result.status == 1
    assert result.flow_order == 1001
    assert result.amount == 5000.0


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatusByCommerceId(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowOrder": 1002,
        "commerceOrder": "OC-002",
        "status": 3,
        "amount": 10000.0,
    }
    mock_get.return_value = mock_response

    result = getStatusByCommerceId(api_client, "OC-002")

    assert isinstance(result, PaymentStatus)
    assert result.status == 3
    assert result.commerce_order == "OC-002"


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatusByFlowOrder(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowOrder": 12345,
        "commerceOrder": "OC-003",
        "status": 2,
        "amount": 3000.0,
    }
    mock_get.return_value = mock_response

    result = getStatusByFlowOrder(api_client, 12345)

    assert isinstance(result, PaymentStatus)
    assert result.status == 2
    assert result.flow_order == 12345


@patch("pyflowcl.Clients.ApiClient.get")
def test_getPayments(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "total": 2,
        "hasMore": False,
        "data": [{"flowOrder": 1}, {"flowOrder": 2}],
    }
    mock_get.return_value = mock_response

    result = getPayments(api_client, {"start": "2023-01-01", "end": "2023-01-31"})

    assert isinstance(result, PaymentList)
    assert result.total == 2
    assert result.hasMore is False
    assert len(result.data) == 2


@patch("pyflowcl.Clients.ApiClient.post")
def test_create(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "url": "https://www.flow.cl/pay",
        "token": "tok_abc123",
        "flowOrder": 9001,
    }
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
    assert result.token == "tok_abc123"
    assert result.flowOrder == 9001


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_injects_api_key_when_missing(mock_post, api_client):
    """api_key from ApiClient is injected when not present in payment_data."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"url": "https://www.flow.cl/pay", "token": "tok_xyz"}
    mock_post.return_value = mock_response

    result = create(api_client, {"commerceOrder": "OC-200", "amount": 500, "subject": "S"})

    assert isinstance(result, PaymentResponse)
    call_kwargs = mock_post.call_args
    posted_data = call_kwargs[0][1] if call_kwargs[0] else call_kwargs[1].get("data", {})
    assert posted_data.get("apiKey") == "test_key"


@patch("pyflowcl.Clients.ApiClient.post")
def test_createEmail(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "url": "https://www.flow.cl/pay",
        "token": "tok_email123",
        "flowOrder": 9002,
    }
    mock_post.return_value = mock_response

    payment_data = {
        "commerceOrder": "OC-456",
        "subject": "Email Payment",
        "amount": 2000,
        "email": "customer@example.com",
        "urlConfirmation": "https://example.com/confirm",
        "urlReturn": "https://example.com/return",
    }
    result = createEmail(api_client, payment_data)

    assert isinstance(result, PaymentResponse)
    assert result.url == "https://www.flow.cl/pay"
    assert result.token == "tok_email123"


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatus_raises_generic_error_on_400(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.text = "Bad request"
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "bad_token")

    assert exc_info.value.code == 400
    assert exc_info.value.message == "Bad request"


@patch("pyflowcl.Clients.ApiClient.get")
def test_getStatus_raises_generic_error_on_500(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "test_token")

    assert exc_info.value.code == 500
    assert exc_info.value.message == "Internal Server Error"
