from sqlalchemy import Column, Computed, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.database import Base


class Bookings(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(ForeignKey("rooms.id"), nullable=False)
    user_id = Column(ForeignKey("users.id"), nullable=False)
    date_from = Column(Date, nullable=False)
    date_to = Column(Date, nullable=False)
    price = Column(Integer, nullable=False)
    total_cost = Column(Integer, Computed("(date_to - date_from) * price"), nullable=False)
    total_days = Column(Integer, Computed("date_to - date_from"), nullable=False)

    room = relationship("Rooms", back_populates="bookings")
    user = relationship("Users", back_populates="bookings")

    def __repr__(self):
        return f"<Booking {self.id}>"
