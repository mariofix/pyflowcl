import hashlib
import hmac
from typing import Any

from .exceptions import ParamsException


def firma_request(params: Any, secret: str) -> str:

    print(f"{params = }")
    string = ""
    for k, d in params.iter():
        string = f"{string}{k}{d}"
    hash_string = hmac.new(secret.encode(), string.encode(), hashlib.sha256).hexdigest()
    return hash_string


def genera_firma(params: dict = None, flow_secret: str = None) -> str:
    if not params or not flow_secret:
        raise ParamsException("Se necesita 'params' y 'flow_secret' para usar esta función")
    string = ""
    for k, d in params.items():
        if d is not None:
            string = f"{string}{k}{d}"
    hash_string = hmac.new(flow_secret.encode(), string.encode(), hashlib.sha256).hexdigest()
    return hash_string


def genera_parametros(params: dict = None, flow_secret: str = None) -> dict:
    if not params or not flow_secret or "apiKey" not in params:
        raise ParamsException("Se necesita 'params' y 'flow_secret' para usar esta función")

    if "apiKey" not in params:
        raise ParamsException("'apiKey' no se encuentra en params")

    # Ordenamos por key
    sorted_params = dict(sorted(params.items(), key=lambda item: item[0]))

    if "s" not in params:
        sorted_params["s"] = genera_firma(params=sorted_params, flow_secret=flow_secret)

    return sorted_params
