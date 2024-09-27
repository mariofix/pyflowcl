import hashlib
import hmac
from dataclasses import dataclass
from typing import Any

import requests


@dataclass
class ApiClient:
    """
    Una clase para interactuar con la API de Flow.cl.

    Attributes:
        api_url (str): La URL base de la API. Por defecto es "https://www.flow.cl/api".
        api_key (str): La clave de la API proporcionada por Flow.cl.
        api_secret (str): El secreto de la API proporcionado por Flow.cl.
    """

    api_url: str = "https://www.flow.cl/api"
    api_key: str = ""
    api_secret: str = ""

    def make_signature(self, params: dict[str, Any]) -> str:
        """
        Genera una firma HMAC-SHA256 para los parámetros dados.

        Args:
            params (dict[str, Any]): Un diccionario de parámetros para firmar.

        Returns:
            str: La firma generada como una cadena hexadecimal.
        """
        string = ""
        for k, d in params.items():
            if d is not None:
                string = string + f"{k}{d}"
        hash_string = hmac.new(self.api_secret.encode(), string.encode(), hashlib.sha256).hexdigest()

        return hash_string

    def get(self, url: str, query_string: dict[str, Any]) -> dict[str, Any]:
        """
        Realiza una solicitud GET a la API.

        Args:
            url (str): La URL específica para la solicitud GET.
            query_string (dict[str, Any]): Los parámetros de consulta para la solicitud.

        Returns:
            dict[str, Any]: La respuesta de la API como un diccionario.
        """
        return requests.get(url, params=query_string)

    def post(self, url: str, post_data: dict[str, Any]) -> dict[str, Any]:
        """
        Realiza una solicitud POST a la API.

        Args:
            url (str): La URL específica para la solicitud POST.
            post_data (dict[str, Any]): Los datos a enviar en el cuerpo de la solicitud POST.

        Returns:
            dict[str, Any]: La respuesta de la API como un diccionario.
        """
        return requests.post(url, data=post_data)
