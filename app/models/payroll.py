from sqlalchemy import Column, Integer, Float, ForeignKey, String
from app.database.db import Base

class Payroll(Base):
    __tablename__ = "payrolls"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    month = Column(String)
    year = Column(Integer)

    basic_salary = Column(Float)
    bonus = Column(Float)
    deductions = Column(Float)
    net_salary = Column(Float) 
