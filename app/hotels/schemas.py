from pydantic import BaseModel, ConfigDict


class SHotel(BaseModel):
    id: int
    name: str
    location: str
    services: list
    image_id: int

    model_config = ConfigDict(from_attributes=True)
