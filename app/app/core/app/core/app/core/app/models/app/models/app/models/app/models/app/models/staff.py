from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.core.db import Base

class Staff(Base):
    __tablename__ = "staff"
    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey("salons.id"))
    name = Column(String)
    active = Column(Boolean, default=True)
