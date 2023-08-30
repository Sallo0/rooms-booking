from sqladmin import ModelView

from app.hotels.models import Hotels


class HotelAdmin(ModelView, model=Hotels):
    column_list = [Hotels.id, Hotels.name, Hotels.location, Hotels.rooms_quantity]
    can_create = True
    can_delete = True
    can_edit = True

    name = "Hotel"
    name_plural = "Hotels"
    icon = "fas fa-hotel"
