"""
pyflowcl.Clients
~~~~~~~~~~~~~~~~
Este modulo implementa el Cliente API genérico.
"""
from dataclasses import dataclass
from typing import Any, Dict

import requests
import hashlib
import hmac
import logging


@dataclass
class ApiClient:
    """Clase ApiClient con los objetos para realizar llamadas

    Implementa todos los métodos de ``dataclass``.

    se instancia con::

        cliente = ApiClient(api_url, api_key, api_secret)

    el cliente luego debe ser entregado como primer parametro de
    las clases incorporadas::

        pay = Payment.create(cliente, [...])

    """

    api_url: str = "https://sandbox.flow.cl/api"
    api_key: str = ""
    api_secret: str = ""

    def make_signature(self, params: Dict[str, Any]) -> str:
        """Crea el Hash de validacion para ser enviado con la informacion

        :rtype: str
        """
        string = ""
        for k, d in params.items():
            if d is not None:
                string = string + f"{k}{d}"
        logging.debug(f"String to Hash: {string}")
        hash_string = hmac.new(
            self.api_secret.encode(), string.encode(), hashlib.sha256
        ).hexdigest()

        return hash_string

    def get(self, url: str, query_string: Dict[str, Any]) -> Dict[str, Any]:
        """Reimplementa get

        :rtype: dict
        """
        return requests.get(url, params=query_string)

    def post(self, url: str, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """Reimplementa post

        :rtype: dict
        """
        return requests.post(url, data=post_data)

    def put(self, url: str, put_data: Dict[str, Any]) -> Dict[str, Any]:
        """Reimplementa put

        :rtype: dict
        """
        return requests.put(url, data=put_data)
