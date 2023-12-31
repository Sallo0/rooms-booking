import pytest
from httpx import AsyncClient

# TODO: разобраться как лучше удалять записи из базы после теста

@pytest.mark.parametrize("email, password, status_code", [
    ("aboba@biba.com", "bibaboba", 200),
    ("aboba@biba.com", "bibaba", 409),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email, password, status_code", [
    ("test@test.com", "test", 200)])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/auth/login", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code
    assert "access_token" in response.json()
