EMPLOYEES = [
    {
        "id": 1,
        "name": "Jeff Bridges",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Kurt Russell",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Morgan Freeman",
        "locationId": 2,
        "customerId": 1
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
