# pyflowcl/Clients.py
"""
##Este Cliente será deprecado en favor de FlowAPI.
Cliente API genérico.

Este modulo contiene

- `ApiClient` - Objeto Principal

__Uso Básico__:
```python
API_URL = "https://www.flow.cl/api"
API_KEY = "your_key"
API_SECRET = "your_secret"
FLOW_TOKEN = "your_payment_token"
api = ApiClient(API_URL, API_KEY, API_SECRET)
```
"""
import hashlib
import hmac
import logging
import warnings
from dataclasses import dataclass
from typing import Any, Dict

import requests


@dataclass
class ApiClient:
    """Clase ApiClient con los objetos para realizar llamadas

    Implementa todos los métodos de ``dataclass``.

    Attributes:
        api_url: URL de API Flow (live o sandbox)
        api_key: APIKey entregado por Flow
        api_secret: SecretKey entregado por Flow
    """

    api_url: str = "https://www.flow.cl/api"
    api_key: str = ""
    api_secret: str = ""

    def __post_init__(self):
        warnings.warn(
            "ApiClient está deprecado, porfavor usa FlowAPI",
            DeprecationWarning,
            stacklevel=2,
        )

    def make_signature(self, params: Dict[str, Any]) -> str:
        """Crea el Hash de validacion para ser enviado con la informacion

        Args:
            params: Parametros para crear la firma

        Returns:
            Hash de validacion
        """
        string = ""
        for k, d in params.items():
            if d is not None:
                string = string + f"{k}{d}"
        logging.debug(f"String to Hash: {string}")
        hash_string = hmac.new(self.api_secret.encode(), string.encode(), hashlib.sha256).hexdigest()

        return hash_string

    def get(self, url: str, query_string: Dict[str, Any]) -> Dict[str, Any]:
        """Reimplementa get

        Args:
            url: URL a obtener
            query_string: diccionario con parametros get

        Returns:
            El objeto `requests`
        """
        return requests.get(url, params=query_string)

    def post(self, url: str, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """Reimplementa post

        Args:
            url: URL a obtener
            post_data: diccionario con parametros post

        Returns:
            El objeto `requests`
        """
        return requests.post(url, data=post_data)

    def put(self, url: str, put_data: Dict[str, Any]) -> Dict[str, Any]:
        """Reimplementa put

        Args:
            url: URL a obtener
            put_data: diccionario con parametros post

        Returns:
            El objeto `requests`
        """
        return requests.put(url, data=put_data)
