from sqlalchemy import select

from app.database import async_session_maker
from app.hotels.models import Hotels
from app.repo.base import BaseRepo


class HotelsRepo(BaseRepo):
    model = Hotels
    pass

    @classmethod
    async def find_by_location_and_time(cls, location, date_from, date_to):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=location)
            result = await session.execute(query)
            return result.scalars().all()

