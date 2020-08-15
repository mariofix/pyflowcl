from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

import requests
import hashlib
import hmac


@dataclass
class ApiClient:
    """ Objeto para definir ApiClient """

    api_url: Optional[str] = None
    api_key: Optional[str] = None
    api_secret: Optional[str] = None

    def make_signature(self, params: Dict[str, Any]) -> str:
        string = ""
        for k, d in params.items():
            string = string + f"{k}{d}"
        hash_string = hmac.new(
            self.api_secret.encode(), string.encode(), hashlib.sha256
        ).hexdigest()

        return hash_string

    def get(self, url: str, query_string: Dict[str, Any]) -> Dict[str, Any]:
        return requests.get(url, params=query_string)
