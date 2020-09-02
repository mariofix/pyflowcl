from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Error:
    """ Objeto para definir un error """

    code: Optional[float] = None
    message: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> Error:
        code = d.get("code")
        message = d.get("message")

        return Error(code=code, message=message,)


@dataclass
class PaymentStatus:
    """ Objeto para obtener el estado de un pago """

    flow_order: Optional[int] = None
    commerce_order: Optional[str] = None
    request_date: Optional[str] = None
    status: Optional[int] = None
    subject: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    payer: Optional[str] = None
    optional: Optional[str] = None
    pending_info: Optional[Dict[Any, Any]] = None
    payment_data: Optional[Dict[Any, Any]] = None
    merchant_id: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentStatus:
        flow_order = d.get("flowOrder")
        commerce_order = d.get("commerceOrder")
        request_date = d.get("requestDate")
        status = d.get("status")
        subject = d.get("subject")
        currency = d.get("currency")
        amount = d.get("amount")
        payer = d.get("payer")
        optional = d.get("optional")
        pending_info = d.get("pending_info")
        payment_data = d.get("paymentData")
        merchant_id = d.get("merchantId")

        return PaymentStatus(
            flow_order=flow_order,
            commerce_order=commerce_order,
            request_date=request_date,
            status=status,
            subject=subject,
            currency=currency,
            amount=amount,
            payer=payer,
            optional=optional,
            pending_info=pending_info,
            payment_data=payment_data,
            merchant_id=merchant_id,
        )


@dataclass
class PaymentRequest:
    """ Objeto para generar una URL de pago """

    amount: float = 0
    apiKey: str = "API_KEY"
    commerceOrder: str = ""
    currency: Optional[str] = None
    email: str = "correo@ejemplo.cl"
    merchantId: Optional[str] = None
    optional: Optional[str] = None
    payment_currency: str = "CLP"
    payment_method: Optional[int] = None
    subject: str = ""
    timeout: Optional[int] = None
    urlConfirmation: str = ""
    urlReturn: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentRequest:
        amount = d.get("amount")
        apiKey = d.get("apiKey")
        commerceOrder = d.get("commerceOrder")
        currency = d.get("currency")
        email = d.get("email")
        merchantId = d.get("merchantId")
        optional = d.get("optional")
        payment_currency = d.get("payment_currency")
        payment_method = d.get("payment_method")
        subject = d.get("subject")
        timeout = d.get("timeout")
        urlConfirmation = d.get("urlConfirmation")
        urlReturn = d.get("urlReturn")
        s = d.get("s")

        return PaymentRequest(
            amount=amount,
            apiKey=apiKey,
            commerceOrder=commerceOrder,
            currency=currency,
            email=email,
            merchantId=merchantId,
            optional=optional,
            payment_currency=payment_currency,
            payment_method=payment_method,
            subject=subject,
            timeout=timeout,
            urlConfirmation=urlConfirmation,
            urlReturn=urlReturn,
            s=s,
        )


@dataclass
class PaymentRequestEmail:
    """ Objeto para generar un correo electronico de pago """

    amount: float = 0
    apiKey: str = "API_KEY"
    commerceOrder: str = ""
    currency: Optional[str] = None
    email: str = "correo@ejemplo.cl"
    forward_days_after: Optional[int] = None
    forward_times: Optional[int] = None
    merchantId: Optional[str] = None
    optional: Optional[str] = None
    payment_currency: Optional[str] = None
    subject: Optional[str] = None
    timeout: Optional[int] = None
    urlConfirmation: str = ""
    urlReturn: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentRequestEmail:
        amount = d.get("amount")
        apiKey = d.get("apiKey")
        commerceOrder = d.get("commerceOrder")
        currency = d.get("currency")
        email = d.get("email")
        forward_days_after = d.get("forward_days_after")
        forward_times = d.get("forward_times")
        merchantId = d.get("merchantId")
        optional = d.get("optional")
        payment_currency = d.get("payment_currency")
        subject = d.get("subject")
        timeout = d.get("timeout")
        urlConfirmation = d.get("urlConfirmation")
        urlReturn = d.get("urlReturn")
        s = d.get("s")

        return PaymentRequestEmail(
            amount=amount,
            apiKey=apiKey,
            commerceOrder=commerceOrder,
            currency=currency,
            email=email,
            forward_days_after=forward_days_after,
            forward_times=forward_times,
            merchantId=merchantId,
            optional=optional,
            payment_currency=payment_currency,
            subject=subject,
            timeout=timeout,
            urlConfirmation=urlConfirmation,
            urlReturn=urlReturn,
            s=s,
        )


@dataclass
class PaymentResponse:
    """ Objeto respuesta de una creacion de pago """

    url: Optional[str] = None
    token: Optional[str] = None
    flowOrder: Optional[float] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentResponse:
        url = d.get("url")
        token = d.get("token")
        flowOrder = d.get("flowOrder")

        return PaymentResponse(url=url, token=token, flowOrder=flowOrder,)


@dataclass
class PaymentList:
    """ Lista de pagos """

    total: Optional[float] = None
    hasMore: Optional[bool] = None
    data: Optional[List[Dict[Any, Any]]] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentList:
        total = d.get("total")
        hasMore = d.get("hasMore")
        data = d.get("data")

        return PaymentList(total=total, hasMore=hasMore, data=data,)
