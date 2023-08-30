from sqladmin import ModelView

from app.hotels.rooms.models import Rooms


class RoomAdmin(ModelView, model=Rooms):
    column_list = [Rooms.id, Rooms.name, Rooms.hotel, Rooms.quantity, Rooms.price]
    can_create = True
    can_delete = True
    can_edit = True

    name = "Room"
    name_plural = "Rooms"
    icon = "fas fa-door-open"
