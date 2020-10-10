CUSTOMERS = [
    {
        "id": 1,
        "name": "Hannah Hall",
        "business": "NSS",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Brain Neal",
        "business": "NSS Day",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "name": "Mitchell Blom",
        "business": "NSS Evening",
        "locationId": 2,
        "customerId": 1
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1

    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)
