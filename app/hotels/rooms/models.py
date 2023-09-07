
from sqlalchemy import JSON, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Rooms(Base):
    __tablename__ = "rooms"
    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[str] = mapped_column(String, nullable=True)
    price: Mapped[int]
    services: Mapped[JSON] = mapped_column(JSON, nullable=True)
    image_id: Mapped[int] = mapped_column(Integer, nullable=True)

    hotel: Mapped["Hotels"] = relationship(back_populates="rooms")
    bookings: Mapped["Bookings"] = relationship(back_populates="room")

    def __repr__(self):
        return f"<Room {self.name if self.name else self.id}>"
