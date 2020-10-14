import sqlite3
import json
from models.employee import Employee

EMPLOYEES = [
    Employee(1, 'Jeff', "404 error street", 1),
    Employee(2, 'Kurt', "404 error street", 2),
    Employee(3, 'Morgan', "404 error street", 1)
]

def get_all_employees():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        """)

        employees = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            employee = Employee(row['id'], row['name'], row['address'],
                            row['location_id'])

            employees.append(employee.__dict__)

    return json.dumps(employees)
    
def get_single_employee(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['name'], data['address'], data['location_id'],
                        data['id'])

        return json.dumps(employee.__dict__)

def create_employee(employee):
    max_id = EMPLOYEES[-1].id
    new_id = max_id + 1
    employee["id"] = new_id
    new_employee = Employee(employee['id'], employee['name'], employee['address'], employee['location_id'])
    EMPLOYEES.append(new_employee)

    return employee

def delete_employee(id):
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)

def update_employee(id, updated_employee):
    for index, employee in enumerate(EMPLOYEES):
        if employee.id == id:
            EMPLOYEES[index] = Employee(updated_employee['id'], updated_employee['name'], updated_employee['address'], updated_employee['location_id'])
            break
