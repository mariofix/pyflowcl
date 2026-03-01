import hashlib
import hmac
from dataclasses import dataclass
from typing import Any

import requests

from .exceptions import ConfigException


@dataclass
class ApiClient:
    """
    Cliente para interactuar con la API de Flow.

    Attributes:
        api_url (str): URL base de la API de Flow. Por defecto es "https://www.flow.cl/api".
        api_key (str | None): Clave de la API de Flow.
        api_secret (str | None): Secreto de la API de Flow.
    """

    api_url: str = "https://www.flow.cl/api"
    api_key: str | None = None
    api_secret: str | None = None

    def make_signature(self, params: dict[str, Any]) -> str:
        """
        Genera una firma HMAC-SHA256 para los parámetros dados.

        Args:
            params (dict[str, Any]): Diccionario de parámetros para firmar.

        Returns:
            str: Firma hexadecimal generada.

        Raises:
            ConfigException: Si api_secret no está configurado.
        """
        if not self.api_secret:
            raise ConfigException("api_secret is required to generate signatures")
        string = "".join(f"{k}{d}" for k, d in params.items() if d)
        return hmac.new(self.api_secret.encode(), string.encode(), hashlib.sha256).hexdigest()

    def get(self, url: str, query_string: dict[str, Any]) -> requests.Response:
        """
        Realiza una solicitud GET a la API de Flow.

        Args:
            url (str): URL relativa para la solicitud.
            query_string (dict[str, Any]): Parámetros de consulta para la solicitud.

        Returns:
            requests.Response: Respuesta de la API.
        """
        return requests.get(url, params=query_string, timeout=5)

    def post(self, url: str, post_data: dict[str, Any]) -> requests.Response:
        """
        Realiza una solicitud POST a la API de Flow.

        Args:
            url (str): URL relativa para la solicitud.
            post_data (dict[str, Any]): Datos a enviar en el cuerpo de la solicitud.

        Returns:
            requests.Response: Respuesta de la API.
        """
        return requests.post(url, data=post_data, timeout=5)
