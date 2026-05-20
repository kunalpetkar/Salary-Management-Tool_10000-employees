from sqlalchemy import Column, Integer, String, Date
from app.database.db import Base

class Leave(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    leave_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String)
