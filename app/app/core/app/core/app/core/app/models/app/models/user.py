from sqlalchemy import Column, Integer, String
from app.core.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    tg_id = Column(String, unique=True, index=True, nullable=False)
    name = Column(String)
    phone = Column(String)
