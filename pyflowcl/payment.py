from dataclasses import asdict
from typing import Any, Dict, List, Optional, Union, cast

from .models import Error, PaymentStatus, PaymentRequest, \
PaymentRequestEmail, PaymentResponse, PaymentList
from .apiclient import ApiClient

def getStatus(
        apiclient: ApiClient, api_key: str, token: str, s: str,
    ) -> Union[
        PaymentStatus, Error, Error,
    ]:
    pass