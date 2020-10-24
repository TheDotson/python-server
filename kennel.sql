        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.customer_id,
            a.location_id,
            l.name location_name,
            l.address location_address,
            c.name customer_name,
            c.address customer_address,
            c.email customer_email,
            c.password customer_password
        FROM animal a
        JOIN Location l
            ON l.id = a.location_id
        JOIN Customer c
            ON c.id = a.customer_id

SELECT * FROM Animal

UPDATE Animal
SET customer_id = 5
WHERE customer_id = 1

SELECT * FROM Customer

DELETE FROM CUSTOMER
WHERE id = 7
