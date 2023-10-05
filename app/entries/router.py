import datetime

from fastapi import APIRouter

from app.entries.dao import EntryDAO
from app.entries.schemas import EntrySchema

router = APIRouter(prefix="/entries", tags=["Entries"])


@router.post("/")
async def add_entry(entry: EntrySchema) -> None:
    """Save entry in DB"""
    await EntryDAO.add(entry)


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
