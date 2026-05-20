def calculate_salary(basic_salary, bonus, deductions):
    net_salary = basic_salary + bonus - deductions

    return {
        "basic_salary": basic_salary,
        "bonus": bonus,
        "deductions": deductions,
        "net_salary": net_salary
    }
