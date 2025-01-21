from dataclasses import dataclass
from typing import Any, Optional


class GenericError(BaseException):
    def __init__(self, data):
        self.code = data.get("code")
        self.message = data.get("message")
        super().__init__(f"{self.code}: {self.message}")

    def __str__(self):
        return f"{self.code}: {self.message}"


@dataclass
class PaymentStatus:
    """
    Representa el estado de un pago en el sistema Flow.cl.

    Esta clase contiene información detallada sobre un pago, incluyendo su estado,
    detalles de la transacción y datos del pagador.

    Attributes:
        flow_order (Optional[int]): Número de orden asignado por Flow.
        commerce_order (Optional[str]): Número de orden asignado por el comercio.
        request_date (Optional[str]): Fecha y hora de la solicitud del pago.
        status (Optional[int]): Estado actual del pago. Los valores posibles son:
            1 (Pagado), 2 (Rechazado), 3 (Pendiente), 4 (Anulado).
        subject (Optional[str]): Asunto o descripción del pago.
        currency (Optional[str]): Código de la moneda utilizada en el pago (ej. CLP, USD).
        amount (Optional[float]): Monto del pago.
        payer (Optional[str]): Correo electrónico o identificación del pagador.
        optional (Optional[str]): Campo para información adicional definida por el comercio.
        pending_info (Optional[dict[Any, Any]]): Información adicional para pagos pendientes.
        payment_data (Optional[dict[Any, Any]]): Datos adicionales relacionados con el método de pago.
        merchant_id (Optional[str]): Identificador único del comercio en Flow.

    Note:
        Todos los campos son opcionales ya que pueden no estar presentes en todas las
        respuestas de la API de Flow, dependiendo del estado y tipo de pago.
    """

    flow_order: Optional[int] = None
    flowOrder: Optional[int] = None
    commerce_order: Optional[str] = None
    commerceOrder: Optional[str] = None
    request_date: Optional[str] = None
    requestDate: Optional[str] = None
    status: Optional[int] = None
    subject: Optional[str] = None
    currency: Optional[str] = None
    amount: Optional[float] = None
    payer: Optional[str] = None
    optional: Optional[str] = None
    pending_info: Optional[dict[Any, Any]] = None
    payment_data: Optional[dict[Any, Any]] = None
    merchant_id: Optional[str] = None

    @staticmethod
    def from_dict(d: dict[str, Any]) -> "PaymentStatus":
        flow_order = d.get("flowOrder")
        flowOrder = d.get("flowOrder")
        commerce_order = d.get("commerceOrder")
        commerceOrder = d.get("commerceOrder")
        request_date = d.get("requestDate")
        requestDate = d.get("requestDate")
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
            flowOrder=flowOrder,
            commerce_order=commerce_order,
            commerceOrder=commerceOrder,
            request_date=request_date,
            requestDate=requestDate,
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
    """
    Representa una solicitud de pago para ser procesada por Flow.cl.

    Esta clase contiene todos los detalles necesarios para iniciar una transacción
    de pago a través de la API de Flow.

    Attributes:
        amount (float): Monto del pago. Valor por defecto es 0.
        commerceOrder (str): Número de orden único asignado por el comercio.
        currency (Optional[str]): Moneda del pago. Si no se especifica, se utilizará
            el valor de payment_currency.
        email (str): Correo electrónico del pagador. Valor por defecto es "correo@ejemplo.cl".
        merchantId (Optional[str]): Identificador único del comercio en Flow.
        optional (Optional[str]): Campo opcional para información adicional definida por el comercio.
        payment_currency (str): Moneda en la que se realizará el pago. Valor por defecto es "CLP".
        payment_method (Optional[int]): Método de pago a utilizar. Los valores posibles dependen
            de la configuración del comercio en Flow.
        subject (str): Asunto o descripción del pago.
        timeout (Optional[int]): Tiempo máximo (en segundos) para completar el pago.
        urlConfirmation (str): URL a la que Flow enviará la confirmación del pago.
        urlReturn (str): URL a la que se redirigirá al usuario después del pago.

    Note:
        Los campos opcionales (currency, merchantId, optional, payment_method, timeout)
        pueden omitirse si no son necesarios para la transacción específica.
    """

    amount: float = 0
    apiKey: Optional[str] = None
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
    def from_dict(d: dict[str, Any]) -> "PaymentRequest":
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
    """
    Representa una solicitud de pago por correo electrónico para ser procesada por Flow.cl.

    Esta clase contiene todos los detalles necesarios para iniciar una transacción de pago
    por correo electrónico a través de la API de Flow. Flow enviará un correo electrónico
    al pagador con la información del pago y un enlace para completar la transacción.

    Attributes:
        amount (float): Monto del pago. Valor por defecto es 0.
        commerceOrder (str): Número de orden único asignado por el comercio.
        currency (Optional[str]): Moneda del pago. Si no se especifica, se utilizará
            el valor de payment_currency.
        email (str): Correo electrónico del pagador. Valor por defecto es "correo@ejemplo.cl".
        forward_days_after (Optional[int]): Número de días después de los cuales se enviará
            un recordatorio si el pago no se ha completado.
        forward_times (Optional[int]): Número de veces que se enviará el recordatorio.
        merchantId (Optional[str]): Identificador único del comercio en Flow.
        optional (Optional[str]): Campo opcional para información adicional definida por el comercio.
        payment_currency (Optional[str]): Moneda en la que se realizará el pago.
        subject (Optional[str]): Asunto o descripción del pago.
        timeout (Optional[int]): Tiempo máximo (en segundos) para completar el pago.
        urlConfirmation (str): URL a la que Flow enviará la confirmación del pago.
        urlReturn (str): URL a la que se redirigirá al usuario después del pago.

    Note:
        Los campos opcionales (currency, forward_days_after, forward_times, merchantId,
        optional, payment_currency, subject, timeout) pueden omitirse si no son necesarios
        para la transacción específica.
        Los campos forward_days_after y forward_times son específicos para el envío
        de recordatorios por correo electrónico.
    """

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
    def from_dict(d: dict[str, Any]) -> "PaymentRequestEmail":
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
    """
    Representa la respuesta a una solicitud de pago procesada por Flow.cl.

    Esta clase contiene la información devuelta por Flow después de iniciar
    una transacción de pago, incluyendo la URL de pago y el token de la transacción.

    Attributes:
        url (Optional[str]): URL a la que se debe redirigir al usuario para completar el pago.
            Puede ser None si la respuesta no incluye una URL.
        token (Optional[str]): Token único que identifica la transacción en el sistema de Flow.
            Puede ser None si la respuesta no incluye un token.
        flowOrder (Optional[int]): Número de orden asignado por Flow a esta transacción.
            Puede ser None si la respuesta no incluye un número de orden.

    Note:
        Todos los campos son opcionales ya que pueden no estar presentes en todas las
        respuestas de la API de Flow, dependiendo del tipo de solicitud y su estado.
    """

    url: Optional[str] = None
    token: Optional[str] = None
    flowOrder: Optional[int] = None

    @staticmethod
    def from_dict(d: dict[str, Any]) -> "PaymentResponse":
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
    """
    Representa una lista paginada de pagos obtenida de Flow.cl.

    Esta clase contiene información sobre un conjunto de pagos, incluyendo
    el número total de pagos, si hay más páginas disponibles, y los datos
    de los pagos en la página actual.

    Attributes:
        total (Optional[int]): El número total de pagos en todas las páginas.
            Puede ser None si la información no está disponible.
        hasMore (Optional[bool]): Indica si hay más páginas de pagos disponibles.
            True si hay más páginas, False si es la última página, None si no se proporciona.
        data (Optional[list[dict[Any, Any]]]): Una lista de diccionarios, donde cada diccionario
            contiene los detalles de un pago individual. Puede ser None si no hay datos disponibles.

    Note:
        - Todos los campos son opcionales ya que pueden no estar presentes en todas las
          respuestas de la API de Flow, dependiendo del contexto de la solicitud.
        - El campo 'data' contiene una lista de diccionarios. Cada diccionario representa
          un pago y su estructura dependerá de la configuración específica de Flow y del
          tipo de información solicitada.
        - Esta clase es útil para manejar respuestas paginadas de la API de Flow,
          permitiendo una fácil navegación a través de múltiples pagos.
    """

    total: Optional[int] = None
    hasMore: Optional[bool] = None
    data: Optional[list[dict[Any, Any]]] = None

    @staticmethod
    def from_dict(d: dict[str, Any]) -> "PaymentList":
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
    amount: float = 0
    apiKey: str = "API_KEY"
    commerceTrxId: Optional[str] = None
    flowTrxId: Optional[float] = None
    receiverEmail: str = "correo@ejemplo.cl"
    refundCommerceOrder: str = ""
    urlCallBack: str = ""
    s: str = ""

    @staticmethod
    def from_dict(d: dict[str, Any]) -> "RefundRequest":
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
    flowRefundOrder: int = 0
    date: str = ""
    status: str = ""
    amount: float = 0
    fee: float = 0

    @staticmethod
    def from_dict(d: dict[str, Any]) -> "RefundStatus":
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
