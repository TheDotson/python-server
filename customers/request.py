from models.customer import Customer

CUSTOMERS = [
    Customer(1, "Hannah Hall", "NSS"),
    Customer(2, "Brain Neal", "NSS Day"),
    Customer(3, "Mitchell Blom", "NSS Evening")
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer.id == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    last_customer = CUSTOMERS[-1]
    new_id = last_customer.id + 1
    customer["id"] = new_id
    new_customer = Customer(customer['id'], customer['name'], customer['business'])
    CUSTOMERS.append(new_customer)

    return customer

def delete_customer(id):
    customer_index = -1

    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            customer_index = index

    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, updated_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            CUSTOMERS[index] = Customer(updated_customer['id'], updated_customer['name'], updated_customer['business'])
            break
