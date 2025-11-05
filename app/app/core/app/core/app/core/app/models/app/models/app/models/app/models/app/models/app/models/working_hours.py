from sqlalchemy import Column, Integer, String, ForeignKey, Time
from app.core.db import Base

class WorkingHours(Base):
    __tablename__ = "working_hours"
    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey("salons.id"))
    weekday = Column(Integer)  # 0=Mon ... 6=Sun
    start_time = Column(String)  # "09:00"
    end_time = Column(String)    # "18:00"
    breaks_json = Column(String, default="[]")
