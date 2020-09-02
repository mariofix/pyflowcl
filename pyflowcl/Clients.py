from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

import requests
import hashlib
import hmac
import logging


@dataclass
class ApiClient:
    """ Objeto para definir ApiClient """

    api_url: str = "https://sandbox.flow.cl/api"
    api_key: str = ""
    api_secret: str = ""

    def make_signature(self, params: Dict[str, Any]) -> str:
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
        return requests.get(url, params=query_string)

    def post(self, url: str, post_data: Dict[str, Any]) -> Dict[str, Any]:
        return requests.post(url, data=post_data)

    def put(self, url: str, put_data: Dict[str, Any]) -> Dict[str, Any]:
        return requests.put(url, data=put_data)
