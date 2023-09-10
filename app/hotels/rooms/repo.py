from datetime import date

from sqlalchemy import select

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.models import Hotels
from app.hotels.rooms.models import Rooms
from app.repo.base import BaseRepo


class RoomsRepo(BaseRepo):
    model = Rooms

    @classmethod
    async def find_all_by_hotel_slug(cls, hotel_slug: str):
        query = (
            select(Rooms.__table__.columns)
            .select_from(Rooms)
            .join(Hotels, Hotels.id == Rooms.hotel_id)
            .filter_by(slug=hotel_slug)
        )
        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def find_one_or_none_by_hotel_slug(cls, hotel_slug: str, room_id: int):
        query = (
            select(Rooms.__table__.columns)
            .select_from(Rooms)
            .join(Hotels, Hotels.id == Rooms.hotel_id)
            .filter_by(slug=hotel_slug, id=room_id)
        )
        async with async_session_maker() as session:
            result = await session.execute(query)
            return result.mappings().first()

    @classmethod
    async def get_free_rooms(cls, hotel_slug: str, date_from: date, date_to: date):
        hotel_rooms_cte = (
            select(Rooms.__table__.columns, Hotels.slug)
            .select_from(Rooms)
            .join(Hotels, Hotels.id == Rooms.hotel_id)
            .filter_by(slug=hotel_slug).cte("hotel_rooms")
        )

        booked_hotel_rooms_cte = (
            select(Bookings.room_id)
            .select_from(Bookings)
            .join(hotel_rooms_cte, Bookings.room_id == hotel_rooms_cte.c.id)
            .where(
                (hotel_rooms_cte.c.slug == hotel_slug)
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
