import json

import pytest
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.status import HTTP_201_CREATED
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.fixture
def api_client():
    email = 'js@js.com'

    user = User.objects.create_user(username='john', email=email, password='js.sj')
    EmailAddress.objects.create(user=user, email=email, primary=True, verified=True)

    client = APIClient()
    # refresh = RefreshToken.for_user(user)
    # client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client


@pytest.mark.django_db
def test_login_response(api_client):
    url = reverse('rest_login')
    response = api_client.post(url, data={"email": "js@js.com", "password": "js.sj"})
    response.render()

    data = json.loads(response.content)

    assert 'accessToken' in data
    assert 'refreshToken' in data
    assert 'user' in data


@pytest.mark.django_db
def test_register_user(api_client):
    url = reverse('rest_register')
    payload = {
        "email": "test@local.com",
        "password1": "t€stPassword",
        "password2": "t€stPassword"
    }
    response = api_client.post(url, data=payload)

    assert response.status_code == HTTP_201_CREATED
