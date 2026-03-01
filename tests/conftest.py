import pytest

from pyflowcl.Clients import ApiClient


@pytest.fixture
def api_client():
    return ApiClient(api_key="test_key", api_secret="test_secret")
