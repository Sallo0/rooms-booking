from sqladmin import ModelView

from app.bookings.models import Bookings


class BookingAdmin(ModelView, model=Bookings):
    column_list = [Bookings.id, Bookings.user, Bookings.room, Bookings.date_from, Bookings.date_to,
                   Bookings.price]
    column_editable_list = [Bookings.date_from, Bookings.date_to, Bookings.price]
    column_filters = [Bookings.date_from, Bookings.date_to, Bookings.price]
    can_create = True

    name = "Booking"
    name_plural = "Bookings"
    icon = "fas fa-calendar-check"
