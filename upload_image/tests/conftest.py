import pytest
from rest_framework.test import APIClient
from .utils import create_user, create_image, create_plan


@pytest.fixture()
def client():
    client = APIClient()
    return client


@pytest.fixture
def set_up():
    create_image()
    create_plan()
    create_user()
