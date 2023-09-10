from datetime import date

from fastapi import APIRouter

from app.hotels.rooms.repo import RoomsRepo as rooms_repo
from app.hotels.rooms.schemas import SRoom

router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int) -> list[SRoom]:
    return await rooms_repo.find_all(hotel_id=hotel_id)


@router.get("/{hotel_id}/rooms/{room_id}")
async def get_room(hotel_id: int, room_id: int) -> SRoom:
    return await rooms_repo.find_one_or_none(hotel_id=hotel_id, room_id=room_id)


@router.post("/{hotel_id}/rooms")
async def add_room():
    pass


@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room():
    pass


@router.put("/{hotel_id}/rooms/{room_id}")
async def update_room():
    pass


@router.get("/{hotel_id}/rooms")
async def get_rooms_by_time(hotel_id: int, date_from: date, date_to: date) -> list[SRoom]:
    return await rooms_repo.get_free_rooms(hotel_id, date_from, date_to)
