from pydantic import BaseModel
from datetime import date

class EmployeeCreate(BaseModel):
    employee_code: str
    first_name: str
    last_name: str
    email: str
    department: str
    designation: str
    joining_date: date
    basic_salary: float
