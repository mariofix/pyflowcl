from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class ApiClient:
    """ Objeto para definir ApiClient """

    base_url: str
