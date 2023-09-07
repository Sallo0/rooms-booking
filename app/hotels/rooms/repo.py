from datetime import date

from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms
from app.repo.base import BaseRepo


class RoomsRepo(BaseRepo):
    model = Rooms

    @classmethod
    async def get_free_rooms(cls, hotel_id: int, date_from: date, date_to: date):
        hotel_rooms_cte = (
            select(Rooms).where(Rooms.hotel_id == hotel_id).cte("hotel_rooms")
        )

        booked_hotel_rooms_cte = (
            select(Bookings.room_id)
            .select_from(Bookings)
            .join(hotel_rooms_cte, Bookings.room_id == hotel_rooms_cte.c.id)
            .where(
                (hotel_rooms_cte.c.hotel_id == hotel_id)
                & (
                    (Bookings.date_from.between(date_from, date_to))
                    | (Bookings.date_to.between(date_from, date_to))
                ),
            )
        ).cte("booked_hotel_rooms")

        result = (
            select(hotel_rooms_cte)
            .select_from(hotel_rooms_cte)
            .where(hotel_rooms_cte.c.id.notin_(select(booked_hotel_rooms_cte)))
        )

        async with async_session_maker() as session:
            result = await session.execute(result)
            return result.mappings().all()
