from datetime import date

from sqlalchemy import func, insert, select

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms
from app.repo.base import BaseRepo


class BookingRepo(BaseRepo):
    model = Bookings

    # TODO: Implement normal logic

    @classmethod
    async def get_free_rooms_amount(cls, room_id: int, date_from: date, date_to: date):
        booked_rooms = select(Bookings).where(
            (room_id == Bookings.room_id) &
            (
                    ((date_from <= Bookings.date_from) & (date_to >= Bookings.date_from)) |
                    ((date_from <= Bookings.date_to) & (date_to >= Bookings.date_to))
            )
        ).cte("booked_rooms")

        rooms_left = select(
            (Rooms.quantity - func.count(booked_rooms.c.room_id)).label("rooms_left")
        ).select_from(Rooms).join(
            booked_rooms, booked_rooms.c.room_id == Rooms.id, isouter=True
        ).where(
            Rooms.id == room_id
        ).group_by(
            Rooms.quantity, booked_rooms.c.room_id
        )

        async with async_session_maker() as session:
            room_left = await session.execute(rooms_left)

        return room_left.scalar()

    @classmethod
    async def add(cls, user_id, room_id: int, date_from: date, date_to: date):

        rooms_left = await cls.get_free_rooms_amount(room_id, date_from, date_to)

        if rooms_left > 0:
            async with async_session_maker() as session:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price = price.scalar()
                add_booking = insert(Bookings).values(
                    user_id=user_id,
                    room_id=room_id,
                    date_from=date_from,
                    date_to=date_to,
                    price=price
                ).returning(Bookings)

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
        else:
            return None
