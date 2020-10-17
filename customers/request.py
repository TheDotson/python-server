import sqlite3
import json
from models.customer import Customer

CUSTOMERS = [
    Customer(1, "Hannah Hall", "404 invalid lane", "hh@nss.com", "password"),
    Customer(2, "Brian Neal", "NSS Day", "bn@nss.com", "password"),
    Customer(3, "Mitchell Blom", "404 invalid lane", "mb@nss.com", "password")
]

def get_all_customers():
    with sqlite3.connect("./kennel.db") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        """)

        customers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            customer = Customer(row['id'], row['name'], row['address'], row['email'], row['password'])

            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
            a.password
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'], data['email'], data['password'])

        return json.dumps(customer.__dict__)


def create_customer(customer):
    last_customer = CUSTOMERS[-1]
    new_id = last_customer.id + 1
    customer["id"] = new_id
    new_customer = Customer(customer['id'], customer['name'], customer['address'], customer['email'], customer['password'])
    CUSTOMERS.append(new_customer)

    return customer

def delete_customer(id):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))


def update_customer(id, updated_customer):
    for index, customer in enumerate(CUSTOMERS):
        if customer.id == id:
            CUSTOMERS[index] = Customer(updated_customer['id'], updated_customer['name'], updated_customer['address'], updated_customer['email'], updated_customer['password'])
            break

def get_customers_by_email(email):

    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'] , row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
