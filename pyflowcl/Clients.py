import hashlib
import hmac
from dataclasses import dataclass
from typing import Any, Optional

import requests


@dataclass
class ApiClient:
    """
    Cliente para interactuar con la API de Flow.

    Attributes:
        api_url (str): URL base de la API de Flow. Por defecto es "https://www.flow.cl/api".
        api_key (str): Clave de la API de Flow.
        api_secret (str): Secreto de la API de Flow.
    """

    api_url: str = "https://www.flow.cl/api"
    api_key: Optional[str] = None
    api_secret: Optional[str] = None

    def make_signature(self, params: dict[str, Any]) -> str:
        """
        Genera una firma HMAC-SHA256 para los parámetros dados.

        Args:
            params (dict[str, Any]): Diccionario de parámetros para firmar.

        Returns:
            str: Firma hexadecimal generada.
        """
        string = ""
        for k, d in params.items():
            if d:
                string = string + f"{k}{d}"
        hash_string = hmac.new(self.api_secret.encode(), string.encode(), hashlib.sha256).hexdigest()

        return hash_string

    def get(self, url: str, query_string: dict[str, Any]) -> dict[str, Any]:
        """
        Realiza una solicitud GET a la API de Flow.

        Args:
            url (str): URL relativa para la solicitud.
            query_string (dict[str, Any]): Parámetros de consulta para la solicitud.

        Returns:
            dict[str, Any]: Respuesta de la API como un diccionario.
        """
        return requests.get(url, params=query_string, timeout=5)

    def post(self, url: str, post_data: dict[str, Any]) -> dict[str, Any]:
        """
        Realiza una solicitud POST a la API de Flow.

        Args:
            url (str): URL relativa para la solicitud.
            post_data (dict[str, Any]): Datos a enviar en el cuerpo de la solicitud.

        Returns:
            dict[str, Any]: Respuesta de la API como un diccionario.
        """
        return requests.post(url, data=post_data, timeout=5)
