from reportlab.pdfgen import canvas

def generate_payslip(employee_name, net_salary):
    file_name = f"{employee_name}_payslip.pdf"

    c = canvas.Canvas(file_name)

    c.drawString(100, 750, f"Employee: {employee_name}")
    c.drawString(100, 720, f"Net Salary: {net_salary}")

    c.save()

    return file_name
