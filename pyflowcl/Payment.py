from dataclasses import asdict
from typing import Any, Dict, List, Optional, Union, cast

from .models import (
    Error,
    PaymentStatus,
    PaymentResponse,
    PaymentList,
)
from .Clients import ApiClient


def get_status(
    apiclient: ApiClient, token: str,
) -> Union[
    PaymentStatus, Error,
]:
    """ Obtiene el estado de un pago previamente creado, el parametro token
    hace referencia a notification id, el cual se recibe luego de procesado
    un pago
    """
    url = f"{apiclient.api_url}/payment/getStatus"

    params: Dict[str, Any] = {
        "apiKey": apiclient.api_key,
        "token": token
    }
    signature = apiclient.make_signature(params)
    params["s"] = signature
    
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def get_status_by_commerce_id(
    apiclient: ApiClient, commerceId: str,
) -> Union[
    PaymentStatus, Error,
]:
    """ Obtiene el estado de un pago previamente creado, el parametro token
    hace referencia a notification id, el cual se recibe luego de procesado
    un pago
    """
    url = f"{apiclient.api_url}/payment/getStatusByCommerceId"

    params: Dict[str, Any] = {
        "apiKey": apiclient.api_key,
        "commerceId": commerceId
    }
    signature = apiclient.make_signature(params)
    params["s"] = signature
    
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def get_status_by_flow_order(
    apiclient: ApiClient, flowOrder: int,
) -> Union[
    PaymentStatus, Error,
]:
    """ Obtiene el estado de un pago previamente creado, el parametro token
    hace referencia a notification id, el cual se recibe luego de procesado
    un pago
    """
    url = f"{apiclient.api_url}/payment/getStatusByFlowOrder"

    params: Dict[str, Any] = {
        "apiKey": apiclient.api_key,
        "flowOrder": flowOrder
    }
    signature = apiclient.make_signature(params)
    params["s"] = signature

    response = apiclient.get(url, params)

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)
