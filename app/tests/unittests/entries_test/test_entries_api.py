import pytest
from httpx import AsyncClient
from test_data import test_add_entry_data


@pytest.mark.parametrize("entry,status_code", test_add_entry_data)
async def test_add_entry(
    entry: dict, status_code: int, authenticated_client: AsyncClient
):
    response = await authenticated_client.post(
        url="/entries/",
        json=entry,
    )
    assert response.status_code == status_code
