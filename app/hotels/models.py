from typing import Optional

from slugify import slugify
from sqlalchemy import JSON, String, event
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[Optional[list[str]]] = mapped_column(JSON)
    slug: Mapped[str] = mapped_column(String, unique=True, index=True)
    image_id: Mapped[Optional[int]]

    rooms: Mapped[list["Rooms"]] = relationship(back_populates="hotel")

    def __repr__(self):
        return f"<Hotel {self.name}>"
