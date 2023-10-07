from sqlalchemy import and_, insert, select, update
from sqlalchemy.orm import selectinload

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.emotions.models import Emotions
from app.entries.exceptions import (
    EntryIsNotExistException,
    IncorrectEntryException,
    UpdatingEntryErrorException,
)
from app.entries.models import Entries
from app.entries.schemas import EntryResponseSchema, EntrySchema
from app.users.models import Users


class EntryDAO(BaseDAO):
    model = Entries

    @classmethod
    async def add(cls, entry: EntrySchema, user: Users) -> int:
        """
        Add data in entry and emotions in DB
        :param entry: entry and list of emotions
        :param user: current user
        :return: entry_id, if entry was saved, or None
        """
        async with (async_session_maker() as session):
            try:
                query_entry = await session.execute(
                    insert(Entries)
                    .values(
                        user_id=user.user_id,
                        date=entry.date.replace(tzinfo=None),
                        situation=entry.situation,
                        thoughts_at_moment=entry.thoughts_at_moment,
                        reaction=entry.reaction,
                        helped_thoughts=entry.helped_thoughts,
                    )
                    .returning(Entries.__table__.c.id)
                )
                entry_id = query_entry.scalar()

                emotions = entry.emotions
                for emotion in emotions:
                    await session.execute(
                        insert(Emotions).values(
                            entry_id=entry_id,
                            emotion=emotion.emotion,
                            rate_at_moment=emotion.rate_at_moment,
                            rate_after=emotion.rate_after,
                        )
                    )
            except Exception:
                await session.rollback()
                raise IncorrectEntryException
            else:
                await session.commit()
                return {"id": entry_id}

    @classmethod
    async def find_all(cls, user: Users) -> list[EntryResponseSchema]:
        """
        SELECT *
        FROM entries
        JOIN emotions ON entries.id == emotions.entry_id
        WHERE entry.user_id == user.user_id;

        Get data about all entries and emotions by current user
        :param user: current user
        :return: list of entries
        """
        async with async_session_maker() as session:
            user_id = user.user_id
            query = (
                select(Entries)
                .join(Emotions, Entries.id == Emotions.entry_id)
                .filter(Entries.user_id == user_id)
            )
            result = await session.execute(
                query.options(selectinload(Entries.emotions))
            )

            return result.unique().scalars().all()

    @classmethod
    async def find_by_id(cls, entry_id: int, user: Users) -> EntryResponseSchema:
        """
        SELECT *
        FROM entries
        JOIN emotions ON entries.id == emotions.entry_id
        WHERE entry.user_id == user.user_id AND entries.id == entry_id;

        Get one entry by id for current user
        :param entry_id: int, id of entry which need to delete
        :param user: current user
        :return: entry with list of emotions
        """
        async with async_session_maker() as session:
            query = (
                select(Entries)
                .join(Emotions, Entries.id == Emotions.entry_id)
                .filter(Entries.id == entry_id, Entries.user_id == user.user_id)
            )
            result = await session.execute(
                query.options(selectinload(Entries.emotions))
            )

            entry = result.unique().scalar_one_or_none()

            if not entry:
                raise EntryIsNotExistException

            return entry

    @classmethod
    async def update(
        cls, entry_id: int, entry: EntryResponseSchema, user: Users
    ) -> int:
        """
        Update entry values and each emotion linked to this entry
        :param entry_id: id of entry
        :param entry: entry with list of emotions
        :param user: current user
        :return: id of updated entry
        """
        async with async_session_maker() as session:
            try:
                entry_update_query = (
                    update(Entries)
                    .where(
                        and_(
                            Entries.id == entry_id,
                            Entries.user_id == user.user_id,
                        )
                    )
                    .values(
                        date=entry.date,
                        situation=entry.situation,
                        thoughts_at_moment=entry.thoughts_at_moment,
                        reaction=entry.reaction,
                        helped_thoughts=entry.helped_thoughts,
                    )
                    .returning(Entries.__table__.c.id)
                )
                result = await session.execute(entry_update_query)

                for emotion_data in entry.emotions:
                    emotion_update_query = (
                        update(Emotions)
                        .where(
                            and_(
                                Emotions.entry_id == entry_id,
                                Emotions.id == emotion_data.id,
                            )
                        )
                        .values(
                            emotion=emotion_data.emotion,
                            rate_at_moment=emotion_data.rate_at_moment,
                            rate_after=emotion_data.rate_after,
                        )
                    )
                    await session.execute(emotion_update_query)
            except Exception:
                raise UpdatingEntryErrorException
            else:
                await session.commit()
                return {"id": result.scalar()}
