from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "User already exists"


class InvalidCredentialsException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid credentials"


class TokenExpiredException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Token expired"


class AbsentTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Absent token"


class InvalidTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Invalid token"


class ForbiddenException(BookingException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = "Forbidden"


class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = "User is not present"


class RoomCanNotBeBookedException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Room can not be booked"
