from pydantic import BaseModel, ConfigDict


class SRoom(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: list
    image_id: int

    model_config = ConfigDict(from_attributes=True)
