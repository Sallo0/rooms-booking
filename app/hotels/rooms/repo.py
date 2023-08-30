from app.hotels.rooms.models import Rooms
from app.repo.base import BaseRepo


class RoomsRepo(BaseRepo):
    model = Rooms
    pass
