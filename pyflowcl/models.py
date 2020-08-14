from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Error:
    """ Objeto para definir un error """

    code: Optional[float] = None
    message: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        code = self.code
        message = self.message

        return {
            "code": code,
            "message": message,
        }

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

    def to_dict(self) -> Dict[str, Any]:
        flow_order = self.flow_order
        commerce_order = self.commerce_order
        request_date = self.request_date
        status = self.status
        subject = self.subject
        currency = self.currency
        amount = self.amount
        payer = self.payer
        optional = self.optional
        pending_info = self.pending_info
        payment_data = self.payment_data
        merchant_id = self.merchant_id

        return {
            "flowOrder": flow_order,
            "commerceOrder": commerce_order,
            "requestDate": request_date,
            "status": status,
            "subject": subject,
            "currency": currency,
            "amount": amount,
            "payer": payer,
            "optional": optional,
            "pending_info": pending_info,
            "paymentData": payment_data,
            "merchantId": merchant_id,
        }

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

    apiKey: Optional[str] = None
    commerceOrder: Optional[str] = None
    subject: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    email: Optional[str] = None
    payment_method: Optional[int] = 9
    urlConfirmation: Optional[str] = None
    urlReturn: Optional[str] = None
    optional: Optional[str] = None
    timeout: Optional[int] = None
    merchantId: Optional[str] = None
    payment_currency: Optional[str] = None
    s: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        apiKey = self.apiKey
        commerceOrder = self.commerceOrder
        subject = self.subject
        currency = self.currency
        amount = self.amount
        email = self.email
        payment_method = self.payment_method
        urlConfirmation = self.urlConfirmation
        urlReturn = self.urlReturn
        optional = self.optional
        timeout = self.timeout
        merchantId = self.merchantId
        payment_currency = self.payment_currency
        s = self.s

        return {
            "apiKey": apiKey,
            "commerceOrder": commerceOrder,
            "subject": subject,
            "currency": currency,
            "amount": amount,
            "email": email,
            "payment_method": payment_method,
            "urlConfirmation": urlConfirmation,
            "urlReturn": urlReturn,
            "optional": optional,
            "timeout": timeout,
            "merchantId": merchantId,
            "payment_currency": payment_currency,
            "s": s,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentRequest:
        apiKey = d.get("apiKey")
        commerceOrder = d.get("commerceOrder")
        subject = d.get("subject")
        currency = d.get("currency")
        amount = d.get("amount")
        email = d.get("email")
        payment_method = d.get("payment_method")
        urlConfirmation = d.get("urlConfirmation")
        urlReturn = d.get("urlReturn")
        optional = d.get("optional")
        timeout = d.get("timeout")
        merchantId = d.get("merchantId")
        payment_currency = d.get("payment_currency")
        s = d.get("s")

        return PaymentRequest(
            apiKey=apiKey,
            commerceOrder=commerceOrder,
            subject=subject,
            currency=currency,
            amount=amount,
            email=email,
            payment_method=payment_method,
            urlConfirmation=urlConfirmation,
            urlReturn=urlReturn,
            optional=optional,
            timeout=timeout,
            merchantId=merchantId,
            payment_currency=payment_currency,
            s=s,
        )


@dataclass
class PaymentRequestEmail:
    """ Objeto para generar un correo electronico de pago """

    apiKey: Optional[str] = None
    commerceOrder: Optional[str] = None
    subject: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    email: Optional[str] = None
    forward_days_after: Optional[int] = None
    forward_times: Optional[int] = None
    urlConfirmation: Optional[str] = None
    urlReturn: Optional[str] = None
    optional: Optional[str] = None
    timeout: Optional[int] = None
    merchantId: Optional[str] = None
    payment_currency: Optional[str] = None
    s: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        apiKey = self.apiKey
        commerceOrder = self.commerceOrder
        subject = self.subject
        currency = self.currency
        amount = self.amount
        email = self.email
        forward_days_after = self.forward_days_after
        forward_times = self.forward_times
        urlConfirmation = self.urlConfirmation
        urlReturn = self.urlReturn
        optional = self.optional
        timeout = self.timeout
        merchantId = self.merchantId
        payment_currency = self.payment_currency
        s = self.s

        return {
            "apiKey": apiKey,
            "commerceOrder": commerceOrder,
            "subject": subject,
            "currency": currency,
            "amount": amount,
            "email": email,
            "forward_days_after": forward_days_after,
            "forward_times": forward_times,
            "urlConfirmation": urlConfirmation,
            "urlReturn": urlReturn,
            "optional": optional,
            "timeout": timeout,
            "merchantId": merchantId,
            "payment_currency": payment_currency,
            "s": s,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentRequestEmail:
        apiKey = d.get("apiKey")
        commerceOrder = d.get("commerceOrder")
        subject = d.get("subject")
        currency = d.get("currency")
        amount = d.get("amount")
        email = d.get("email")
        forward_days_after = d.get("forward_days_after")
        forward_times = d.get("forward_times")
        urlConfirmation = d.get("urlConfirmation")
        urlReturn = d.get("urlReturn")
        optional = d.get("optional")
        timeout = d.get("timeout")
        merchantId = d.get("merchantId")
        payment_currency = d.get("payment_currency")
        s = d.get("s")

        return PaymentRequest(
            apiKey=apiKey,
            commerceOrder=commerceOrder,
            subject=subject,
            currency=currency,
            amount=amount,
            email=email,
            forward_days_after=forward_days_after,
            forward_times=forward_times,
            urlConfirmation=urlConfirmation,
            urlReturn=urlReturn,
            optional=optional,
            timeout=timeout,
            merchantId=merchantId,
            payment_currency=payment_currency,
            s=s,
        )


@dataclass
class PaymentResponse:
    """ Objeto respuesta de una creacion de pago """

    url: Optional[str] = None
    token: Optional[str] = None
    flowOrder: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        url = self.url
        token = self.token
        flowOrder = self.flowOrder

        return {
            "url": url,
            "token": token,
            "flowOrder": flowOrder,
        }

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

    def to_dict(self) -> Dict[str, Any]:
        total = self.total
        hasMore = self.hasMore
        if self.data is None:
            data = None
        else:
            data = self.data

        return {
            "total": total,
            "hasMore": hasMore,
            "data": data,
        }

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> PaymentList:
        total = d.get("total")
        hasMore = d.get("hasMore")
        data = d.get("data")

        return PaymentList(total=total, hasMore=hasMore, data=data,)
