from dataclasses import asdict
from typing import Any, Dict, Union, cast
from .Clients import ApiClient
import logging
import sys

if sys.version_info[0] == 3 and sys.version_info[1] < 7:
    from .models_36 import *
else:
    from .models import *


def getStatus(
    apiclient: ApiClient, token: str,
) -> Union[
    PaymentStatus, Error,
]:
    """ Obtiene el estado de un pago previamente creado, el parametro token
    hace referencia a notification id, el cual se recibe luego de procesado
    un pago
    """
    url = f"{apiclient.api_url}/payment/getStatus"

    params: Dict[str, Any] = {"apiKey": apiclient.api_key, "token": token}
    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def getStatusByCommerceId(
    apiclient: ApiClient, commerceId: str,
) -> Union[
    PaymentStatus, Error,
]:
    """ Obtiene el estado de un pago previamente creado, el parametro token
    hace referencia a notification id, el cual se recibe luego de procesado
    un pago
    """
    url = f"{apiclient.api_url}/payment/getStatusByCommerceId"

    params: Dict[str, Any] = {"apiKey": apiclient.api_key, "commerceId": commerceId}
    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def getStatusByFlowOrder(
    apiclient: ApiClient, flowOrder: int,
) -> Union[
    PaymentStatus, Error,
]:
    """ Obtiene el estado de un pago previamente creado, el parametro token
    hace referencia a notification id, el cual se recibe luego de procesado
    un pago
    """
    url = f"{apiclient.api_url}/payment/getStatusByFlowOrder"

    params: Dict[str, Any] = {"apiKey": apiclient.api_key, "flowOrder": flowOrder}
    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def getPayments(
    apiclient: ApiClient, payment_info: Dict[str, Any]
) -> Union[
    PaymentList, Error,
]:
    """
    Este método permite obtener la lista paginada de pagos recibidos en
    un día.Los objetos pagos de la lista tienen la misma estructura de
    los retornados en los servicios payment/getStatus
    """
    url = f"{apiclient.api_url}/payment/getPayments"

    payment_info["apiKey"] = apiclient.api_key
    signature = apiclient.make_signature(payment_info)
    payment_info["s"] = signature
    logging.debug("Before Request:" + str(payment_info))
    response = apiclient.get(url, payment_info)

    if response.status_code == 200:
        return PaymentList.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def create(
    apiclient: ApiClient, payment_data: Dict[str, Any]
) -> Union[
    PaymentResponse, Error,
]:
    """
    Este método permite crear una orden de pago a Flow y recibe como respuesta
    la URL para redirigir el browser del pagador y el token que identifica la
    transacción. La url de redirección se debe formar concatenando los valores
    recibidos en la respuesta de la siguiente forma:

    url + "?token=" +token

    Una vez que el pagador efectúe el pago, Flow notificará el resultado a la
    página del comercio que se envió en el parámetro urlConfirmation.
    """
    url = f"{apiclient.api_url}/payment/create"
    payment = PaymentRequest.from_dict(payment_data)
    if payment.apiKey is None:
        payment.apiKey = apiclient.api_key

    payment.s = apiclient.make_signature(asdict(payment))

    logging.debug("Before Request:" + str(payment))

    response = apiclient.post(url, asdict(payment))

    if response.status_code == 200:
        return PaymentResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def createEmail(
    apiclient: ApiClient, payment_data: Dict[str, Any]
) -> Union[
    PaymentResponse, Error,
]:
    """
    Permite generar un cobro por email. Flow emite un email al pagador
    que contiene la información de la Orden de pago y el link de pago
    correspondiente. Una vez que el pagador efectúe el pago, Flow
    notificará el resultado a la página del comercio que se envió en el
    parámetro urlConfirmation.
    """
    url = f"{apiclient.api_url}/payment/createEmail"
    payment = PaymentRequestEmail.from_dict(payment_data)
    if payment.apiKey is None:
        payment.apiKey = apiclient.api_key

    payment.s = apiclient.make_signature(asdict(payment))

    logging.debug("Before Request:" + str(payment))

    response = apiclient.post(url, asdict(payment))

    if response.status_code == 200:
        return PaymentResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)
