import uuid

from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


from sqlalchemy.orm import relationship

from db.base_class import Base


class Exam(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(200), nullable=False)
    description = Column(String(500))

    slots = relationship("ExamSlot", back_populates="exam")


class ExamSlot(Base):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    exam_id = Column(UUID(as_uuid=True), ForeignKey('exam.id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    max_capacity = Column(Integer, default=50000)

    exam = relationship("Exam", back_populates="slots")
    reservations = relationship("Reservation", back_populates="slot")