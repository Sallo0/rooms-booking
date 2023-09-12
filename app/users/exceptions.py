from fastapi import status

from app.exceptions import BookingException


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
