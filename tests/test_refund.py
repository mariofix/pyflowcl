from unittest.mock import MagicMock, patch

import pytest

from pyflowcl.models import GenericError, RefundStatus
from pyflowcl.Refund import create, getStatus


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowRefundOrder": 1234567,
        "date": "2023-06-01",
        "amount": 1000.0,
        "status": "accepted",
        "fee": 50.0,
    }
    mock_post.return_value = mock_response

    result = create(api_client, {"amount": 1000.0, "receiverEmail": "receiver@example.com"})

    assert isinstance(result, RefundStatus)
    assert result.flowRefundOrder == 1234567
    assert result.amount == 1000.0
    assert result.status == "accepted"
    assert result.fee == 50.0


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund_injects_api_key_when_missing(mock_post, api_client):
    """api_key from ApiClient is injected when not present in refund_data."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowRefundOrder": 999,
        "date": "2023-06-01",
        "amount": 500.0,
        "status": "pending",
        "fee": 0.0,
    }
    mock_post.return_value = mock_response

    result = create(api_client, {"amount": 500.0})

    assert isinstance(result, RefundStatus)
    call_kwargs = mock_post.call_args
    posted_data = call_kwargs[0][1] if call_kwargs[0] else call_kwargs[1].get("data", {})
    assert posted_data.get("apiKey") == "test_key"


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund_raises_generic_error_on_400(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.text = "Invalid refund parameters"
    mock_post.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        create(api_client, {"amount": 1000.0})

    assert exc_info.value.code == 400
    assert exc_info.value.message == "Invalid refund parameters"


@patch("pyflowcl.Clients.ApiClient.post")
def test_create_refund_raises_generic_error_on_500(mock_post, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_post.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        create(api_client, {"amount": 1000.0})

    assert exc_info.value.code == 500
    assert exc_info.value.message == "Internal Server Error"


@patch("pyflowcl.Clients.ApiClient.get")
def test_get_refund_status(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "flowRefundOrder": 1234567,
        "date": "2023-06-01",
        "amount": 1000.0,
        "status": "accepted",
        "fee": 25.0,
    }
    mock_get.return_value = mock_response

    result = getStatus(api_client, "TEST_TOKEN")

    assert isinstance(result, RefundStatus)
    assert result.flowRefundOrder == 1234567
    assert result.amount == 1000.0
    assert result.status == "accepted"


@patch("pyflowcl.Clients.ApiClient.get")
def test_get_refund_status_raises_generic_error_on_401(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_response.text = "Unauthorized access"
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "BAD_TOKEN")

    assert exc_info.value.code == 401
    assert exc_info.value.message == "Unauthorized access"


@patch("pyflowcl.Clients.ApiClient.get")
def test_get_refund_status_raises_generic_error_on_500(mock_get, api_client):
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.text = "Internal Server Error"
    mock_get.return_value = mock_response

    with pytest.raises(GenericError) as exc_info:
        getStatus(api_client, "TEST_TOKEN")

    assert exc_info.value.code == 500
    assert exc_info.value.message == "Internal Server Error"
