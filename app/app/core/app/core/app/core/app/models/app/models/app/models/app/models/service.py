from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.db import Base

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey("salons.id"))
    name = Column(String, nullable=False)
    duration_min = Column(Integer, default=30)
    buffer_min = Column(Integer, default=0)
    price = Column(Integer, default=0)
