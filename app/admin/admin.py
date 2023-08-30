from sqladmin import Admin

from app.admin.auth import authentication_backend
from app.admin.booking_admin import BookingAdmin
from app.admin.hotel_admin import HotelAdmin
from app.admin.room_admin import RoomAdmin
from app.admin.user_admin import UserAdmin
from app.api import app
from app.database import engine

admin = Admin(
    app=app,
    engine=engine,
    authentication_backend=authentication_backend,
    title="Hotel API", base_url="/admin")

admin.add_view(UserAdmin)
admin.add_view(HotelAdmin)
admin.add_view(RoomAdmin)
admin.add_view(BookingAdmin)
