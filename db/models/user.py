import uuid

from db.base_class import Base
from sqlalchemy import Column, UUID
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role = Column(String(10), nullable=False)

    reservations = relationship("Reservation", back_populates="user")