from fastapi import APIRouter, Depends, status

from app.entries.dao import EntryDAO
from app.entries.schemas import EntryIdSchema, EntryResponseSchema, EntrySchema
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/entries", tags=["Entries"])


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=EntryIdSchema)
async def add_entry(entry: EntrySchema, user: Users = Depends(get_current_user)) -> int:
    """
    Save entry and emotions in DB
    :param entry: entry and list of emotions
    :param user: current user
    :return: id of added entry
    """
    return await EntryDAO.add(entry, user)


@router.get(
    "/", status_code=status.HTTP_200_OK, response_model=list[EntryResponseSchema]
)
async def get_all_entries(
    user: Users = Depends(get_current_user),
) -> list[EntryResponseSchema]:
    """
    Get all entries for user
    :param user: current user
    :return: list of entries with emotions
    """
    return await EntryDAO.find_all(user)


@router.get(
    "/{entry_id}", status_code=status.HTTP_200_OK, response_model=EntryResponseSchema
)
async def get_entry_by_id(
    entry_id: int, user: Users = Depends(get_current_user)
) -> EntryResponseSchema:
    """
    Get entry by id
    :param entry_id: int, entry id
    :param user: current user
    :return: entry with emotions
    """
    return await EntryDAO.find_by_id(entry_id, user)


@router.delete("/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_entry(entry_id: int, user: Users = Depends(get_current_user)) -> None:
    """
    Delete entry and list of emotions by entry_id
    :param entry_id: int, id of entry which need to delete
    :param user: current user
    :return: entry id which was updated
    """
    return await EntryDAO.delete(id=entry_id, user_id=user.user_id)


@router.put(
    "/{entry_id}", status_code=status.HTTP_202_ACCEPTED, response_model=EntryIdSchema
)
async def update_entry(
    entry_id: int, entry: EntryResponseSchema, user: Users = Depends(get_current_user)
) -> int:
    """
    Update entry and list of emotions by entry_id
    :param entry_id: id of entry
    :param entry: entry which need to update
    :param user: current user
    :return: entry id which was updated
    """
    return await EntryDAO.update(entry_id, entry, user)
