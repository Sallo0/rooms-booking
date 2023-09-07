from sqlalchemy import select

from app.database import async_session_maker
from app.hotels.models import Hotels
from app.repo.base import BaseRepo
from app.hotels.rooms.repo import RoomsRepo as rooms_repo


class HotelsRepo(BaseRepo):
    model = Hotels

    @classmethod
    async def find_by_location_and_time(cls, location, date_from, date_to):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(id=location)
            hotels = await session.execute(query)
            hotels = hotels.scalars().all()

        hotels = [
            hotel
            for hotel in hotels
            if await rooms_repo.get_free_rooms(hotel.id, date_from, date_to)
        ]

        return hotels