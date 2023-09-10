from datetime import date

from fastapi import APIRouter

from app.hotels.repo import HotelsRepo as hotels_repo
from app.hotels.schemas import SHotel, SHotelUpdate

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get("")
async def get_hotels() -> list[SHotel]:
    return await hotels_repo.find_all()


@router.get("/{hotel_id}")
async def get_hotel(hotel_id: int) -> SHotel:
    return await hotels_repo.find_by_id(hotel_id)


@router.get("")
async def get_hotels_by_location_and_time(location: str, date_from: date, date_to: date) -> list[SHotel]:
    return await hotels_repo.find_by_location_and_time(location, date_from, date_to)


@router.post("")
async def add_hotel(hotel: SHotel) -> SHotel:
    return await hotels_repo.add(**hotel.model_dump(exclude={"id"}))


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id: int):
    pass


@router.put("/{hotel_id}")
async def update_hotel(hotel_id: int, hotel: SHotelUpdate) -> SHotel:
    return await hotels_repo.update_by_id(hotel_id, **hotel.model_dump(exclude_unset=True))
