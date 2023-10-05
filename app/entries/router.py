from typing import Union

from fastapi import APIRouter, Depends

from app.entries.dao import EntryDAO
from app.entries.schemas import EntrySchema
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(prefix="/entries", tags=["Entries"])


@router.post("/")
async def add_entry(
    entry: EntrySchema, user: Users = Depends(get_current_user)
) -> Union[int, None]:
    """Save entry in DB"""
    return await EntryDAO.add(entry, user)


@router.get("/")
async def find_all_entries_for_user(user_id: int) -> list[EntrySchema]:
    """
    Get all entries for current user
    :param user_id: int, id of current user
    :return: list of entries with emotions
    """
    pass


@router.get("/{entry_id}")
async def find_entry_by_id(entry_id: int) -> EntrySchema:
    """
    Get entry by id
    :param id: int, entry id
    :return: entry with emotions
    """
    pass
