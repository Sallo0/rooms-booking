from datetime import date

from fastapi import APIRouter

from app.hotels.rooms.repo import RoomsRepo as rooms_repo
from app.hotels.rooms.schemas import SRoom

router = APIRouter(prefix="/hotels", tags=["Rooms"])


@router.get("/{hotel_slug}/rooms")
async def get_rooms(hotel_slug: str) -> list[SRoom]:
    return await rooms_repo.find_all_by_hotel_slug(hotel_slug)


@router.get("/{hotel_slug}/rooms/{room_id}")
async def get_room(hotel_slug: str, room_id: int) -> SRoom:
    return await rooms_repo.find_one_or_none_by_hotel_slug(
        hotel_slug=hotel_slug, room_id=room_id
    )


@router.post("/{hotel_id}/rooms")
async def add_room():
    pass


@router.delete("/{hotel_id}/rooms/{room_id}")
async def delete_room():
    pass


@router.put("/{hotel_id}/rooms/{room_id}")
async def update_room():
    pass


@router.get("/{hotel_slug}/rooms")
async def get_rooms_by_time(
    hotel_slug: str, date_from: date, date_to: date
) -> list[SRoom]:
    return await rooms_repo.get_free_rooms(hotel_slug, date_from, date_to)
