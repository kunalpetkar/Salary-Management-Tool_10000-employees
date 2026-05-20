from sqlalchemy import Column, Integer, Date, Float
from app.database.db import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    attendance_date = Column(Date)
    working_hours = Column(Float)
