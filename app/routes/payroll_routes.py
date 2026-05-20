from fastapi import APIRouter
from app.services.payroll_service import calculate_salary

router = APIRouter()

@router.post("/process-payroll")
def process_payroll(
    basic_salary: float,
    bonus: float,
    deductions: float
):
    return calculate_salary(
        basic_salary,
        bonus,
        deductions
    )
