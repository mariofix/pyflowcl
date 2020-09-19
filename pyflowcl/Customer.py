from dataclasses import asdict
from typing import Any, Dict, Union, cast

from .models import (
    Error,
    Customer,
    CustomerRequest,
    CustomerList,
    CustomerRegisterResponse,
    CustomerRegisterStatusResponse,
    PaymentStatus,
    CustomerChargeRequest,
    CollectRequest,
    CollectResponse,
    BatchCollectRequest,
    BatchCollectResponse,
)
from .Clients import ApiClient
import logging


def create(
    apiclient: ApiClient, customer_data: Dict[str, Any]
) -> Union[
    Customer, Error,
]:
    """
    Permite crear clientes para efectuarles cargos recurrentes o suscribirlos
    a un planes de suscripción. Una vez creado un cliente, Flow lo identificará
    por un hash denominado customerId, ejemplo:

    customerId: cus_onoolldvec
    """
    url = f"{apiclient.api_url}/customer/create"

    customer = CustomerRequest.from_dict(customer_data)
    if customer.apiKey is None:
        customer.apiKey = apiclient.api_key
    customer.s = apiclient.make_signature(asdict(customer))
    logging.debug("Before Request:" + str(customer))

    response = apiclient.post(url, asdict(customer))

    if response.status_code == 200:
        return Customer.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def edit(
    apiclient: ApiClient, customer_data: Dict[str, Any]
) -> Union[
    Customer, Error,
]:
    """
    Este servicio permite editar los datos de un cliente
    """
    url = f"{apiclient.api_url}/customer/edit"

    customer = CustomerRequest.from_dict(customer_data)
    if customer.apiKey is None:
        customer.apiKey = apiclient.api_key
    customer.s = apiclient.make_signature(asdict(customer))
    logging.debug("Before Request:" + str(customer))

    response = apiclient.post(url, asdict(customer))

    if response.status_code == 200:
        return Customer.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def delete(
    apiclient: ApiClient, customer_data: Dict[str, Any]
) -> Union[
    Customer, Error,
]:
    """
    Este servicio permite editar los datos de un cliente
    """
    url = f"{apiclient.api_url}/customer/delete"

    customer = CustomerRequest.from_dict(customer_data)
    if customer.apiKey is None:
        customer.apiKey = apiclient.api_key
    customer.s = apiclient.make_signature(asdict(customer))
    logging.debug("Before Request:" + str(customer))

    response = apiclient.post(url, asdict(customer))

    if response.status_code == 200:
        return Customer.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def get(
    apiclient: ApiClient, cust_id: str,
) -> Union[
    Customer, Error,
]:
    """
    Permite obtener los datos de un cliente en base a su customerId.
    """
    url = f"{apiclient.api_url}/customer/get"

    params: Dict[str, Any] = {"apiKey": apiclient.api_key, "customerId": cust_id}
    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return Customer.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def list(
    apiclient: ApiClient, filter_params: Dict[str, Any],
) -> Union[
    CustomerList, Error,
]:
    """
    Permite obtener los datos de un cliente en base a su customerId.
    """

    url = f"{apiclient.api_url}/customer/list"

    params: Dict[str, Any] = {"apiKey": apiclient.api_key}
    # params.update(filter_params) retorna None, Plan B:
    req_params = {**params, **filter_params}

    signature = apiclient.make_signature(req_params)
    req_params["s"] = signature
    logging.debug("Before Request:" + str(req_params))
    response = apiclient.get(url, req_params)

    if response.status_code == 200:
        return CustomerList.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def register(
    apiclient: ApiClient, customerId: str, url_return: str
) -> Union[
    CustomerRegisterResponse, Error,
]:
    """
    Envía a un cliente a registrar su tarjeta de crédito para poder
    efectuarle cargos automáticos. El servicio responde con la URL para
    redirigir el browser del pagador y el token que identifica la
    transacción. La url de redirección se debe formar concatenando los
    valores recibidos en la respuesta de la siguiente forma:

    url + "?token=" +token

    Una vez redirigido el browser del cliente, Flow responderá por medio de
    una llamada POST a la url callback del comercio indicada en el parámetro
    url_return pasando como parámetro token. El comercio debe implementar
    una página y capturar el parámetro token enviado por Flow para luego
    consumir el servicio "customer/getRegisterStatus" para obtener el
    resultado del registro.
    """

    url = f"{apiclient.api_url}/customer/register"

    params: Dict[str, Any] = {
        "apiKey": apiclient.api_key,
        "customerId": customerId,
        "url_return": url_return,
    }

    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.post(url, params)

    if response.status_code == 200:
        return CustomerRegisterResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def getRegisterStatus(
    apiclient: ApiClient, token: str
) -> Union[
    CustomerRegisterStatusResponse, Error,
]:
    """
    Elte servicio retorna el resultado del registro de la tarjeta de
    crédito de un cliente.
    """

    url = f"{apiclient.api_url}/customer/getRegisterStatus"

    params: Dict[str, Any] = {
        "apiKey": apiclient.api_key,
        "token": token,
    }

    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.get(url, params)

    if response.status_code == 200:
        return CustomerRegisterStatusResponse.from_dict(
            cast(Dict[str, Any], response.json())
        )
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def unRegister(
    apiclient: ApiClient, customerId: str
) -> Union[
    Customer, Error,
]:
    """
    Este servicio permite eliminar el registro de la tarjeta de crédito
    de un cliente. Al eliminar el registro no se podrá hacer cargos
    automáticos y Flow enviará un cobro por email.
    """

    url = f"{apiclient.api_url}/customer/unRegister"

    params: Dict[str, Any] = {
        "apiKey": apiclient.api_key,
        "customerId": customerId,
    }

    signature = apiclient.make_signature(params)
    params["s"] = signature
    logging.debug("Before Request:" + str(params))
    response = apiclient.post(url, params)

    if response.status_code == 200:
        return Customer.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def charge(
    apiclient: ApiClient, charge_data: Dict[str, Any]
) -> Union[
    PaymentStatus, Error,
]:
    """
    Este servicio permite efectuar un cargo automático en la tarjeta de
    crédito previamente registrada por el cliente. Si el cliente no
    tiene registrada una tarjeta el metodo retornará error.
    """

    url = f"{apiclient.api_url}/customer/charge"

    charge = CustomerChargeRequest.from_dict(charge_data)
    if charge.apiKey is None:
        charge.apiKey = apiclient.api_key
    charge.s = apiclient.make_signature(asdict(charge))
    logging.debug("Before Request:" + str(charge))

    response = apiclient.post(url, asdict(charge))

    if response.status_code == 200:
        return PaymentStatus.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def collect(
    apiclient: ApiClient, collect_data: Dict[str, Any]
) -> Union[
    CollectResponse, Error,
]:
    """
    Este servicio envía un cobro a un cliente. Si el cliente tiene
    registrada una tarjeta de crédito se le hace un cargo automático, si
    no tiene registrada una tarjeta de credito se genera un cobro. Si se
    envía el parámetro byEmail = 1, se genera un cobro por email.
    """

    url = f"{apiclient.api_url}/customer/collect"

    collect = CollectRequest.from_dict(collect_data)
    if collect.apiKey is None:
        collect.apiKey = apiclient.api_key
    collect.s = apiclient.make_signature(asdict(collect))
    logging.debug("Before Request:" + str(collect))

    response = apiclient.post(url, asdict(collect))

    if response.status_code == 200:
        return CollectResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)


def batchCollect(
    apiclient: ApiClient, collect_data: Dict[str, Any]
) -> Union[
    BatchCollectResponse, Error,
]:
    """
    Este servicio envía de forma masiva un lote de cobros a clientes.
    Similar al servicio collect pero masivo y asíncrono. Este servicio
    responde con un token identificador del lote y el número de filas
    recibidas.
    """

    url = f"{apiclient.api_url}/customer/batchCollect"

    batch_collect = BatchCollectRequest.from_dict(collect_data)
    if batch_collect.apiKey is None:
        batch_collect.apiKey = apiclient.api_key
    batch_collect.s = apiclient.make_signature(asdict(batch_collect))
    logging.debug("Before Request:" + str(batch_collect))

    response = apiclient.post(url, asdict(batch_collect))

    if response.status_code == 200:
        return BatchCollectResponse.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 400:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    if response.status_code == 401:
        return Error.from_dict(cast(Dict[str, Any], response.json()))
    else:
        raise Exception(response=response)
