from models.employee import Employee

EMPLOYEES = [
    Employee(1, 'Jeff', 2, True, True, 20),
    Employee(2, 'Kurt', 1, False, True, 13),
    Employee(3, 'Morgan', 3, False, False, 15)
]


def get_all_employees():
    return EMPLOYEES

def create_employee(employee):
    max_id = EMPLOYEES[-1].id

    new_id = max_id + 1

    employee["id"] = new_id

    new_employee = Employee(employee['id'], employee['name'], employee['location'], employee['manager'], employee['full_time'], employee['hourly_rate'])
    EMPLOYEES.append(new_employee)

    return employee

    
def get_single_employee(id):
   
    requested_employee = None

    for employee in EMPLOYEES:
        if employee.id == id:
            requested_employee = employee

    return requested_employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            EMPLOYEES[index] = Employee(new_employee['id'], new_employee['name'], new_employee['location'], new_employee['manager'], new_employee['full_time'], new_employee['hourly_rate'])
            break
