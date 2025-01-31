from dataclasses import asdict
from typing import Any, cast

from .Clients import ApiClient
from .models import GenericError, RefundRequest, RefundStatus


def create(apiclient: ApiClient, refund_data: dict[str, Any]) -> RefundStatus:
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
    response = apiclient.post(url, asdict(refund))
    if response.status_code == 200:
        return RefundStatus.from_dict(cast(dict[str, Any], response.json()))
    else:
        raise GenericError({"code": response.status_code, "message": response})


def getStatus(apiclient: ApiClient, token: str) -> RefundStatus:
    """
    Permite obtener el estado de un reembolso solicitado. Este servicio
    se debe invocar desde la página del comercio que se señaló en el
    parámetro urlCallback del servicio refund/create.
    """
    url = f"{apiclient.api_url}/refund/getStatus"

    params: dict[str, Any] = {"apiKey": apiclient.api_key, "token": token}
    signature = apiclient.make_signature(params)
    params["s"] = signature
    response = apiclient.get(url, params)
    if response.status_code == 200:
        return RefundStatus.from_dict(cast(dict[str, Any], response.json()))
    else:
        raise GenericError({"code": response.status_code, "message": response})
