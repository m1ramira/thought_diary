import pytest

from app.users.dao import UsersDAO


@pytest.mark.parametrize("user_id,is_present", [(1, True), (2, True), (4, False)])
async def test_find_by_id(user_id, is_present):
    user = await UsersDAO.find_by_id(user_id)

    if is_present:
        assert user
        assert user.user_id == user_id
    else:
        assert not user
