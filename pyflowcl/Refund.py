from dataclasses import asdict
from typing import Any, Dict, Union, cast

from .models import Error, RefundRequest, RefundStatus
from .Clients import ApiClient
import logging


def create(
    apiclient: ApiClient, refund_data: Dict[str, Any]
) -> Union[
    RefundStatus, Error,
]:
    """
    Este servicio permite crear una orden de reembolso. Una vez que el
    receptor del reembolso acepte o rechaze el reembolso, Flow
    notificará vía POST a la página del comercio identificada en
    urlCallback pasando como parámetro token

    En esta página, el comercio debe invocar el servicio refund/getStatus
    para obtener el estado del reembolso.
    """
    url = f"{apiclient.api_url}/refund/create"
    refund = RefundRequest.from_dict(refund_data)
    if refund.apiKey is None:
        refund.apiKey = apiclient.api_key
    refund.s = apiclient.make_signature(asdict(refund))
    logging.debug("Before Request:" + str(refund))

    response = apiclient.post(url, asdict(refund))

    if response.status_code == 200:
        return RefundStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def getStatus(
    apiclient: ApiClient, token: str,
) -> Union[
    RefundStatus, Error,
]:
    """
    Permite obtener el estado de un reembolso solicitado. Este servicio
    se debe invocar desde la página del comercio que se señaló en el
    parámetro urlCallback del servicio refund/create.
    """
    url = f"{apiclient.api_url}/refund/getStatus"

    params: Dict[str, Any] = {"apiKey": apiclient.api_key, "token": token}
    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return RefundStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)
