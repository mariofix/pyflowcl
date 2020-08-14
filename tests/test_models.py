from pyflow.models import Error, PaymentList, PaymentResponse


def test_error_object():
    e = Error()
    assert e == Error(code=None, message=None)


def test_error_to_dict():
    e = Error()
    assert e.to_dict() == {"code": None, "message": None}


def test_error_from_dict():
    e = Error()
    base_dict = {"code": None, "message": None}
    assert e.from_dict(base_dict) == Error(code=None, message=None)


def test_payment_list_object():
    p = PaymentList()
    assert p == PaymentList(total=None, hasMore=None, data=None)


def test_payment_list_to_dict():
    p = PaymentList()
    assert p.to_dict() == {"total": None, "hasMore": None, "data": None}


def test_payment_list_from_dict():
    p = PaymentList()
    base_dict = {"total": None, "hasMore": None, "data": None}
    assert p.from_dict(base_dict) == PaymentList(total=None, hasMore=None, data=None)


def test_payment_response_object():
    p = PaymentResponse()
    assert p == PaymentResponse(url=None, token=None, flowOrder=None,)


def test_payment_response_to_dict():
    p = PaymentResponse()
    assert p.to_dict() == {"url": None, "token": None, "flowOrder": None}


def test_payment_response_from_dict():
    p = PaymentResponse()
    base_dict = {"url": None, "token": None, "flowOrder": None}
    assert p.from_dict(base_dict) == PaymentResponse(
        url=None, token=None, flowOrder=None,
    )
