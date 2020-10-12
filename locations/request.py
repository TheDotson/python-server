from models.location import Location

LOCATIONS = [
    Location(1, "Nashville North", "8422 Johnson Pike"),
    Location(2, 'Nashville South', "209 Emory Drive"),
    Location(3, 'Nashville West', "100 Charlotte Pike")
]

def get_all_locations():
    return LOCATIONS

def create_location(location):
    max_id = LOCATIONS[-1].id

    new_id = max_id + 1

    location["id"] = new_id

    new_location = Location(location['id'], location['name'], location['address'])
    LOCATIONS.append(new_location)

    return location

    
def get_single_location(id):
   
    requested_location = None

    for location in LOCATIONS:
        if location.id == id:
            requested_location = location

    return requested_location

def delete_location(id):
    location_index = -1

    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            location_index = index

    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    for index, location in enumerate(LOCATIONS):
        if location.id == id:
            LOCATIONS[index] = Location(new_location['id'], new_location['name'], new_location['address'])
            break
