from sqlalchemy import Column, Integer, String, Float, Date
from app.database.db import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_code = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
    designation = Column(String)
    joining_date = Column(Date)
    basic_salary = Column(Float)
