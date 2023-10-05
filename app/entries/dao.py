from sqlalchemy import insert

from app.dao.base import BaseDAO
from app.database import async_session_maker
from app.emotions.models import Emotions
from app.entries.exceptions import IncorrectEntryException
from app.entries.models import Entries
from app.entries.schemas import EntrySchema


class EntryDAO(BaseDAO):
    model = Entries

    @classmethod
    async def add(cls, entry: EntrySchema) -> None:
        """
        Add data in entry and emotions in DB
        :param entry: entry and list of emotions
        :return: None
        """
        async with (async_session_maker() as session):
            try:
                query_entry = await session.execute(
                    insert(Entries)
                    .values(
                        user_id=entry.user_id,
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
                            emotion=emotion.emotion_name,
                            rate_at_moment=emotion.rate_at_moment,
                            rate_after=emotion.rate_after,
                        )
                    )
            except Exception:
                await session.rollback()
                raise IncorrectEntryException
            else:
                await session.commit()
