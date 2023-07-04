# pyflowcl/utils.py
"""
Utilidades para pyflow

Este modulo contiene

- `genera_firma()` - Funcion para generar hash de validacion
- `genera_parametros()` - Funcion para generar parametros a enviar

"""
import hashlib
import hmac

from .exceptions import ParamsException


def genera_firma(params: dict = None, flow_secret: str = None) -> str:
    """Crea el Hash de validacion

    Args:
        params: Parametros para crear la firma
        flow_secret: secretKey de Flow

    Returns:
        Hash de validacion

    Raises:
        ParamsException: Si `params` o `flow_key` no están definidos
    """
    if not params or not flow_secret:
        raise ParamsException("Se necesita 'params' y 'flow_secret' para usar esta función")
    string = ""
    for k, d in params.items():
        if d is not None:
            string = f"{string}{k}{d}"
    hash_string = hmac.new(flow_secret.encode(), string.encode(), hashlib.sha256).hexdigest()
    return hash_string


def genera_parametros(params: dict = None, flow_secret: str = None) -> dict:
    """Normaliza y genera los parametros para las llamadas

    Este esta funcion verifica que los parametros se encuentren ordenados
    alfabéticamente, para luego generar el hash de validacion

    Args:
        params: Parametros para crear la firma
        flow_secret: secretKey de Flow

    Returns:
        `dict` ordenado alfabeticamente con `apiKey` y `s` incorporados

    Raises:
        ParamsException: Si `params` o `flow_secret` no están definidos
    """
    if not params or not flow_secret or "apiKey" not in params:
        raise ParamsException("Se necesita 'params' y 'flow_secret' para usar esta función")

    if "apiKey" not in params:
        raise ParamsException("'apiKey' no se encuentra en params")

    # Ordenamos por key
    sorted_params = dict(sorted(params.items(), key=lambda item: item[0]))

    if "s" not in params:
        sorted_params["s"] = genera_firma(params=sorted_params, flow_secret=flow_secret)

    return sorted_params
