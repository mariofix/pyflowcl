from pyflowcl.models import Error, PaymentList, PaymentResponse


def test_error_object():
    e = Error()
    assert e == Error(code=None, message=None)
    base_dict = {"code": None, "message": None}
    assert e.from_dict(base_dict) == Error(code=None, message=None)


def test_payment_list_object():
    p = PaymentList()
    assert p == PaymentList(total=None, hasMore=None, data=None)
    base_dict = {"total": None, "hasMore": None, "data": None}
    assert p.from_dict(base_dict) == PaymentList(total=None, hasMore=None, data=None)


def test_payment_response_object():
    p = PaymentResponse()
    assert p == PaymentResponse(url=None, token=None, flowOrder=None,)
    base_dict = {"url": None, "token": None, "flowOrder": None}
    assert p.from_dict(base_dict) == PaymentResponse(
        url=None, token=None, flowOrder=None,
    )
