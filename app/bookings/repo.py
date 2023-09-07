from datetime import date

from sqlalchemy import func, insert, select

from app.bookings.models import Bookings
from app.database import async_session_maker
from app.hotels.rooms.models import Rooms
from app.repo.base import BaseRepo


class BookingRepo(BaseRepo):
    model = Bookings

    @classmethod
    async def find_all(cls, **filters):
        async with async_session_maker() as session:
            query = (
                select(
                    Bookings.__table__.columns,
                    Rooms.__table__.columns,
                )
                .select_from(Bookings)
                .join(Rooms, Rooms.id == Bookings.room_id)
                .filter_by(**filters)
            )
            result = await session.execute(query)
            return result.mappings().all()

    @classmethod
    async def is_room_free(cls, room_id: int, date_from: date, date_to: date):
        room_bookings = select(func.count(Bookings.id)).where(
            (room_id == Bookings.room_id)
            & (
                ((date_from <= Bookings.date_from) & (date_to >= Bookings.date_from))
                | ((date_from <= Bookings.date_to) & (date_to >= Bookings.date_to))
            )
        )

        async with async_session_maker() as session:
            room_bookings_amount = await session.execute(room_bookings)

        return room_bookings_amount.scalar() == 0

    @classmethod
    async def add(cls, user_id, room_id: int, date_from: date, date_to: date):
        room_free = await cls.is_room_free(room_id, date_from, date_to)

        if room_free:
            async with async_session_maker() as session:
                get_price = select(Rooms.price).filter_by(id=room_id)
                price = await session.execute(get_price)
                price = price.scalar()
                add_booking = (
                    insert(Bookings)
                    .values(
                        user_id=user_id,
                        room_id=room_id,
                        date_from=date_from,
                        date_to=date_to,
                        price=price,
                    )
                    .returning(Bookings)
                )

                new_booking = await session.execute(add_booking)
                await session.commit()
                return new_booking.scalar()
        else:
            return None
