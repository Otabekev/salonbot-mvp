from sqlalchemy import Column, Integer, String
from app.core.db import Base

class Salon(Base):
    __tablename__ = "salons"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    tz = Column(String, default="Asia/Tashkent")
    address = Column(String)
