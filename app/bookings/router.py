from datetime import date

from fastapi import APIRouter, Depends

from app.bookings.repo import BookingRepo as booking_repo
from app.bookings.schemas import SBooking
from app.exceptions import RoomCanNotBeBookedException
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
# @cache(expire=60)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    return await booking_repo.find_all(user_id=user.id)


@router.get("/{booking_id}")
async def get_booking(booking_id: int) -> SBooking:
    return await booking_repo.find_by_id(booking_id)


@router.post("")
async def add_booking(room_id: int, date_from: date, date_to: date,
                      user: Users = Depends(get_current_user)) -> SBooking:
    booking = await booking_repo.add(user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to)
    if not booking:
        raise RoomCanNotBeBookedException

    bookings_dict = SBooking.model_validate(booking).model_dump()
    send_booking_confirmation_email.delay(bookings_dict, user.email)

    return booking


@router.delete("/{booking_id}")
async def delete_booking(booking_id: int, user: Users = Depends(get_current_user)):
    return await booking_repo.delete(id=booking_id)


@router.put("/{booking_id}")
async def update_booking(booking_id: int, user: Users = Depends(get_current_user)):
    pass
