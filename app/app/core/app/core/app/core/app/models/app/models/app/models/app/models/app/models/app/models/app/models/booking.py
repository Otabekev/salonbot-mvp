from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.core.db import Base

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True)
    salon_id = Column(Integer, ForeignKey("salons.id"))
    staff_id = Column(Integer, ForeignKey("staff.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    service_id = Column(Integer, ForeignKey("services.id"))
    start_dt_utc = Column(DateTime, nullable=False)
    end_dt_utc = Column(DateTime, nullable=False)
    status = Column(String, default="confirmed")
    notes = Column(String, default="")
    gcal_event_id = Column(String, default="")
