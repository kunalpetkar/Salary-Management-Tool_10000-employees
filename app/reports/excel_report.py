import pandas as pd

def export_payroll_report(data):
    df = pd.DataFrame(data)

    df.to_excel(
        "payroll_report.xlsx",
        index=False
    )
