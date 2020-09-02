from pyflowcl.models import (
    Error,
    PaymentList,
    PaymentResponse,
    PaymentRequest,
    PaymentRequestEmail,
    RefundRequest,
    RefundStatus,
)


def test_model_error():
    e = Error()
    assert e.code is None
    assert e.message is None


def test_model_payment_list():
    p = PaymentList()
    assert p.total is None
    assert p.hasMore is None
    assert p.data is None


def test_model_payment_response():
    p = PaymentResponse()
    assert p.url is None
    assert p.token is None
    assert p.flowOrder is None


def test_model_payment_request():
    p = PaymentRequest()
    assert p.amount == 0
    assert p.apiKey == "API_KEY"
    assert p.email == "correo@ejemplo.cl"
    assert p.urlConfirmation == ""
    assert p.urlReturn == ""
    assert p.subject == ""
    assert p.s == ""
    assert p.payment_currency == "CLP"
    assert p.currency is None
    assert p.merchantId is None
    assert p.optional is None
    assert p.payment_method is None
    assert p.timeout is None


def test_model_payment_request_email():
    p = PaymentRequestEmail()
    assert p.amount == 0
    assert p.apiKey == "API_KEY"
    assert p.email == "correo@ejemplo.cl"
    assert p.urlConfirmation == ""
    assert p.urlReturn == ""
    assert p.s == ""
    assert p.forward_days_after is None
    assert p.forward_times is None
    assert p.merchantId is None
    assert p.optional is None
    assert p.payment_currency is None
    assert p.subject is None
    assert p.timeout is None


def test_model_refund_request():
    p = RefundRequest()
    assert p.amount == 0
    assert p.apiKey == "API_KEY"
    assert p.receiverEmail == "correo@ejemplo.cl"
    assert p.refundCommerceOrder == ""
    assert p.urlCallback == ""
    assert p.s == ""
    assert p.commerceTrxId is None
    assert p.flowTrxId is None


def test_model_refund_status():
    p = RefundStatus()
    assert p.flowRefundOrder == 0
    assert p.date == ""
    assert p.status == ""
    assert p.amount == 0
    assert p.fee == 0
