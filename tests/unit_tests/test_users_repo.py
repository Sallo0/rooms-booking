import pytest

from app.users.repo import UsersRepo as users_repo


@pytest.mark.parametrize("user_id, email, is_exists", [
    (1, "test@test.com", True),
    (2, "sergay@example.com", True),
    (4, "unlisted@user.com", False),
])
async def test_find_user_by_id(user_id, email, is_exists):
    user = await users_repo.find_by_id(user_id)
    if is_exists:
        assert user
        assert user.email == email
    else:
        assert not user
