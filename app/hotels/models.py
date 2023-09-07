from sqlalchemy import JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[JSON] = mapped_column(JSON)
    image_id: Mapped[int]

    rooms: Mapped["Rooms"] = relationship(back_populates="hotel")

    def __repr__(self):
        return f"<Hotel {self.name}>"
