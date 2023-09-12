from fastapi import status

from app.exceptions import BookingException


class RoomCanNotBeBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Room can not be booked"