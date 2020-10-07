LOCATIONS = [
    {
        "id": 1,
        "city": "Nashville",
        "locationId": 1,
        "customerId": 4
    },
    {
        "id": 2,
        "city": "Denver",
        "locationId": 1,
        "customerId": 2
    },
    {
        "id": 3,
        "city": "Portland",
        "locationId": 2,
        "customerId": 1
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location
