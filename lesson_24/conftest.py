import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.fixture(scope="class")
def session():

    session = requests.Session()

    response = session.post(
        "http://127.0.0.1:8080/auth",
        auth=HTTPBasicAuth(
            "test_user",
            "test_pass"
        )
    )

    assert response.status_code == 200

    access_token = response.json()["access_token"]
    session.headers.update({
        "Authorization": f"Bearer {access_token}"
    })
    return session
