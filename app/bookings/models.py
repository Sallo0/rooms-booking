from datetime import date

from sqlalchemy import Column, Computed, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Bookings(Base):
    __tablename__ = "bookings"
    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date]
    date_to: Mapped[date]
    price: Mapped[int]
    total_cost = Column(Integer, Computed("(date_to - date_from) * price"), nullable=False)
    total_days = Column(Integer, Computed("date_to - date_from"), nullable=False)

    room: Mapped["Rooms"] = relationship(back_populates="bookings")
    user: Mapped["Users"] = relationship(back_populates="bookings")

    def __repr__(self):
        return f"<Booking {self.id}>"
