"""
pyflowcl.models
~~~~~~~~~~~~~~~~
Modelos de distintos objetos del paquete
"""
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, cast


class GenericError(BaseException):
    def __init__(self, data):
        self.code = data.get("code")
        self.message = data.get("message")
        super().__init__(f"{self.code}: {self.message}")

    def __str__(self):
        return f"{self.code}: {self.message}"


@dataclass
class PaymentStatus:
    """Objeto para obtener el estado de un pago"""

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
    def from_dict(d: Dict[str, Any]) -> "PaymentStatus":
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
    """Objeto para generar una URL de pago"""

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
    def from_dict(d: Dict[str, Any]) -> "PaymentRequest":
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
    """Objeto para generar un correo electronico de pago"""

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
    def from_dict(d: Dict[str, Any]) -> "PaymentRequestEmail":
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
    """Objeto respuesta de una creacion de pago"""

    url: Optional[str] = None
    token: Optional[str] = None
    flowOrder: Optional[float] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "PaymentResponse":
        url = d.get("url")
        token = d.get("token")
        flowOrder = d.get("flowOrder")

        return PaymentResponse(
            url=url,
            token=token,
            flowOrder=flowOrder,
        )


@dataclass
class PaymentList:
    """Lista de pagos"""

    total: Optional[float] = None
    hasMore: Optional[bool] = None
    data: Optional[List[Dict[Any, Any]]] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "PaymentList":
        total = d.get("total")
        hasMore = d.get("hasMore")
        data = d.get("data")

        return PaymentList(
            total=total,
            hasMore=hasMore,
            data=data,
        )


@dataclass
class RefundRequest:
    """Refund  Request object"""

    amount: float = 0
    apiKey: str = "API_KEY"
    commerceTrxId: Optional[str] = None
    flowTrxId: Optional[float] = None
    receiverEmail: str = "correo@ejemplo.cl"
    refundCommerceOrder: str = ""
    urlCallBack: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RefundRequest":
        amount = d.get("amount")
        apiKey = d.get("apiKey")
        commerceTrxId = d.get("commerceTrxId")
        flowTrxId = d.get("flowTrxId")
        receiverEmail = d.get("receiverEmail")
        refundCommerceOrder = d.get("refundCommerceOrder")
        urlCallBack = d.get("urlCallBack")
        s = d.get("s")

        return RefundRequest(
            amount=amount,
            apiKey=apiKey,
            commerceTrxId=commerceTrxId,
            flowTrxId=flowTrxId,
            receiverEmail=receiverEmail,
            refundCommerceOrder=refundCommerceOrder,
            urlCallBack=urlCallBack,
            s=s,
        )


@dataclass
class RefundStatus:
    """Refund object"""

    flowRefundOrder: int = 0
    date: str = ""
    status: str = ""
    amount: float = 0
    fee: float = 0

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "RefundStatus":
        flowRefundOrder = d.get("flowRefundOrder")
        date = d.get("date")
        status = d.get("status")
        amount = d.get("amount")
        fee = d.get("fee")

        return RefundStatus(
            flowRefundOrder=flowRefundOrder,
            date=date,
            status=status,
            amount=amount,
            fee=fee,
        )


@dataclass
class Customer:
    """Customer Object"""

    created: str = ""
    creditCardType: Optional[str] = None
    customerId: str = ""
    email: str = ""
    externalId: Optional[str] = None
    last4CardDigits: Optional[str] = None
    name: str = ""
    pay_mode: Optional[str] = None
    registerDate: Optional[str] = None
    status: int = 0

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "Customer":
        created = d.get("created")
        creditCardType = d.get("creditCardType")
        customerId = d.get("customerId")
        email = d.get("email")
        externalId = d.get("externalId")
        last4CardDigits = d.get("last4CardDigits")
        name = d.get("name")
        pay_mode = d.get("pay_mode")
        registerDate = d.get("registerDate")
        status = d.get("status")

        return Customer(
            created=created,
            creditCardType=creditCardType,
            customerId=customerId,
            email=email,
            externalId=externalId,
            last4CardDigits=last4CardDigits,
            name=name,
            pay_mode=pay_mode,
            registerDate=registerDate,
            status=status,
        )


@dataclass
class CustomerRequest:
    """CustomerRequest Object"""

    apiKey: str = ""
    customerId: str = ""
    email: str = ""
    externalId: str = ""
    name: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CustomerRequest":
        apiKey = d.get("apiKey")
        customerId = d.get("customerId")
        email = d.get("email")
        externalId = d.get("externalId")
        name = d.get("name")
        s = d.get("s")

        return CustomerRequest(
            apiKey=apiKey,
            customerId=customerId,
            email=email,
            externalId=externalId,
            name=name,
            s=s,
        )


@dataclass
class CustomerList:
    """Lista de Clientes"""

    total: Optional[float] = None
    hasMore: Optional[bool] = None
    data: Optional[List[Dict[Any, Any]]] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CustomerList":
        total = d.get("total")
        hasMore = d.get("hasMore")
        data = d.get("data")

        return CustomerList(
            total=total,
            hasMore=hasMore,
            data=data,
        )


@dataclass
class CustomerRegisterResponse:
    """Objeto respuesta"""

    url: Optional[str] = None
    token: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CustomerRegisterResponse":
        url = d.get("url")
        token = d.get("token")

        return CustomerRegisterResponse(
            url=url,
            token=token,
        )


@dataclass
class CustomerRegisterStatusResponse:
    """Objeto respuesta"""

    creditCardType: str = ""
    customerId: str = ""
    last4CardDigits: str = ""
    status: int = 0

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CustomerRegisterStatusResponse":
        creditCardType = d.get("creditCardType")
        customerId = d.get("customerId")
        last4CardDigits = d.get("last4CardDigits")
        status = d.get("status")

        return CustomerRegisterStatusResponse(
            creditCardType=creditCardType,
            customerId=customerId,
            last4CardDigits=last4CardDigits,
            status=status,
        )


@dataclass
class CustomerChargeRequest:
    """Objeto para generar una URL de pago"""

    amount: float = 0
    apiKey: str = "API_KEY"
    commerceOrder: str = ""
    currency: Optional[str] = None
    optionals: Optional[str] = None
    subject: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CustomerChargeRequest":
        amount = d.get("amount")
        apiKey = d.get("apiKey")
        commerceOrder = d.get("commerceOrder")
        currency = d.get("currency")
        optionals = d.get("optionals")
        subject = d.get("subject")
        s = d.get("s")

        return CustomerChargeRequest(
            amount=amount,
            apiKey=apiKey,
            commerceOrder=commerceOrder,
            currency=currency,
            optionals=optionals,
            subject=subject,
            s=s,
        )


@dataclass
class CollectResponse:
    """Objeto para CollectResponse"""

    commerce_order: Optional[str] = None
    flow_order: Optional[float] = None
    paymen_result: Optional[PaymentStatus] = None
    status: Optional[int] = None
    token: Optional[str] = None
    type: Optional[float] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CollectResponse":
        type = d.get("type")
        commerce_order = d.get("commerceOrder")
        flow_order = d.get("flowOrder")
        url = d.get("url")
        token = d.get("token")
        status = d.get("status")
        paymen_result = None
        if d.get("paymenResult") is not None:
            paymen_result = PaymentStatus.from_dict(cast(Dict[str, Any], d.get("paymenResult")))

        return CollectResponse(
            type=type,
            commerce_order=commerce_order,
            flow_order=flow_order,
            url=url,
            token=token,
            status=status,
            paymen_result=paymen_result,
        )


@dataclass
class CollectRequest:
    """Objeto para generar un correo electronico de pago"""

    amount: float = 0
    apiKey: str = "API_KEY"
    byEmail: Optional[int] = None
    commerceOrder: str = ""
    currency: Optional[str] = None
    customerId: str = ""
    forward_days_after: Optional[int] = None
    forward_times: Optional[int] = None
    ignore_auto_charging: Optional[int] = None
    merchantId: Optional[str] = None
    optionals: Optional[str] = None
    paymentMethod: Optional[int] = 9
    subject: Optional[str] = None
    timeout: Optional[int] = None
    urlConfirmation: str = ""
    urlReturn: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CollectRequest":
        amount = d.get("amount")
        apiKey = d.get("apiKey")
        byEmail = d.get("byEmail")
        commerceOrder = d.get("commerceOrder")
        currency = d.get("currency")
        forward_days_after = d.get("forward_days_after")
        forward_times = d.get("forward_times")
        ignore_auto_charging = d.get("ignore_auto_charging")
        merchantId = d.get("merchantId")
        optionals = d.get("optionals")
        subject = d.get("subject")
        timeout = d.get("timeout")
        urlConfirmation = d.get("urlConfirmation")
        urlReturn = d.get("urlReturn")
        s = d.get("s")

        return CollectRequest(
            amount=amount,
            apiKey=apiKey,
            byEmail=byEmail,
            commerceOrder=commerceOrder,
            currency=currency,
            ignore_auto_charging=ignore_auto_charging,
            forward_days_after=forward_days_after,
            forward_times=forward_times,
            merchantId=merchantId,
            optionals=optionals,
            subject=subject,
            timeout=timeout,
            urlConfirmation=urlConfirmation,
            urlReturn=urlReturn,
            s=s,
        )


@dataclass
class CollectObject:
    """Objeto de cobro para un lote de cobros"""

    customer_id: str
    commerce_order: str
    subject: str
    amount: float
    currency: Optional[str] = None
    payment_method: Optional[float] = None
    optional: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "CollectObject":
        customer_id = d.get("customerId")
        commerce_order = d.get("commerceOrder")
        subject = d.get("subject")
        amount = d.get("amount")
        currency = d.get("currency")
        payment_method = d.get("paymentMethod")
        optional = d.get("optional")

        return CollectObject(
            customer_id=customer_id,
            commerce_order=commerce_order,
            subject=subject,
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            optional=optional,
        )


@dataclass
class BatchCollectRequest:
    apiKey: str = "API_KEY"
    batchRows: str = ""
    byEmail: int = 0
    forward_days_after: Optional[int] = None
    forward_times: Optional[int] = None
    timeout: Optional[int] = None
    urlCallBack: str = ""
    urlConfirmation: str = ""
    urlReturn: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BatchCollectRequest":
        apiKey = d.get("apiKey")
        batchRows = d.get("batchRows")
        byEmail = d.get("byEmail")
        forward_days_after = d.get("forward_days_after")
        forward_times = d.get("forward_times")
        timeout = d.get("timeout")
        urlCallBack = d.get("urlCallBack")
        urlConfirmation = d.get("urlConfirmation")
        urlReturn = d.get("urlReturn")
        s = d.get("s")

        return BatchCollectRequest(
            apiKey=apiKey,
            batchRows=batchRows,
            byEmail=byEmail,
            forward_days_after=forward_days_after,
            forward_times=forward_times,
            timeout=timeout,
            urlCallBack=urlCallBack,
            urlConfirmation=urlConfirmation,
            urlReturn=urlReturn,
            s=s,
        )


@dataclass
class BatchCollectRejectedRow:
    customerId: Optional[str] = None
    commerceOrder: Optional[str] = None
    rowNumber: Optional[int] = None
    parameter: Optional[str] = None
    errorCode: Optional[int] = None
    errorMsg: Optional[str] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BatchCollectRejectedRow":
        customerId = d.get("customerId")
        commerceOrder = d.get("commerceOrder")
        rowNumber = d.get("rowNumber")
        parameter = d.get("parameter")
        errorCode = d.get("errorCode")
        errorMsg = d.get("errorMsg")

        return BatchCollectRejectedRow(
            customerId=customerId,
            commerceOrder=commerceOrder,
            rowNumber=rowNumber,
            parameter=parameter,
            errorCode=errorCode,
            errorMsg=errorMsg,
        )


@dataclass
class BatchCollectResponse:
    token: Optional[str] = None
    receivedRows: Optional[int] = None
    acceptedRows: Optional[int] = None
    rejectedRows: Optional[List[BatchCollectRejectedRow]] = None

    @staticmethod
    def from_dict(d: Dict[str, Any]) -> "BatchCollectResponse":
        token = d.get("token")
        receivedRows = d.get("receivedRows")
        acceptedRows = d.get("acceptedRows")
        rejectedRows = []
        for rejected_row in d.get("rejectedRows") or []:
            rejected_row_item = BatchCollectRejectedRow.from_dict(rejected_row)

            rejectedRows.append(rejected_row_item)

        return BatchCollectResponse(
            token=token,
            receivedRows=receivedRows,
            acceptedRows=acceptedRows,
            rejectedRows=rejectedRows,
        )
