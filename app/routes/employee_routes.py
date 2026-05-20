from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import SessionLocal
from app.models.employee import Employee
from app.schemas.employee_schema import EmployeeCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/employees")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(**employee.dict())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee

@router.get("/employees")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()
