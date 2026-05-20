from fastapi import FastAPI
from app.routes import employee_routes
from app.routes import payroll_routes

app = FastAPI(
    title="Salary Management Tool"
)

app.include_router(employee_routes.router)
app.include_router(payroll_routes.router)

@app.get("/")
def root():
    return {
        "message": "Salary Management Tool Running"
    }
