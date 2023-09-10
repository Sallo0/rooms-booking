from datetime import date

from sqlalchemy import func, select

from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.repo import RoomsRepo as rooms_repo
from app.repo.base import BaseRepo


class HotelsRepo(BaseRepo):
    model = Hotels

    @classmethod
    async def find_by_location_and_time(cls, location: str, date_from: date, date_to: date):
        async with async_session_maker() as session:
            query = select(cls.model).filter(
                func.to_tsvector(
                    "russian", func.concat(Hotels.location, " ", Hotels.name)
                ).match(location, postgresql_regconfig="russian")
            )

            hotels = await session.execute(query)
            hotels = hotels.scalars().all()

        hotels = [
            hotel
            for hotel in hotels
            if await rooms_repo.get_free_rooms(hotel.slug, date_from, date_to)
        ]

        return hotels
