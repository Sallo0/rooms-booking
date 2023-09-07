from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

# TODO: add slug


class Hotels(Base):
    __tablename__ = "hotels"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    image_id = Column(Integer)
    rooms = relationship("Rooms", back_populates="hotel")

    def __repr__(self):
        return f"<Hotel {self.name}>"
