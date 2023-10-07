import pytest
from httpx import AsyncClient
from test_data import test_add_entry_data, test_update_entry_data


@pytest.mark.parametrize("entry,status_code", test_add_entry_data)
async def test_add_entry(
    entry: dict, status_code: int, authenticated_client: AsyncClient
):
    response = await authenticated_client.post(
        url="/entries/",
        json=entry,
    )

    assert response.status_code == status_code
    if response.status_code == 201:
        assert "id" in response.json()


async def test_get_all_entries(authenticated_client: AsyncClient):
    response = await authenticated_client.get(
        url="/entries/",
    )
    assert response.status_code == 200
    assert response.json() is not None


@pytest.mark.parametrize("entry_id,status_code", [(4, 200), (5, 404)])
async def test_get_entry_by_id(
    entry_id, status_code, authenticated_client: AsyncClient
):
    response = await authenticated_client.get(
        url=f"/entries/{entry_id}",
    )
    assert response.status_code == status_code
    if response.status_code == 200:
        assert response.json() is not None


@pytest.mark.parametrize("entry_id,entry,status_code", test_update_entry_data)
async def test_update_entry(
    entry_id: int, entry: dict, status_code: int, authenticated_client: AsyncClient
):
    response = await authenticated_client.put(
        url=f"/entries/{entry_id}",
        json=entry,
    )

    assert response.status_code == status_code
    if response.status_code == 202:
        assert "id" in response.json()
