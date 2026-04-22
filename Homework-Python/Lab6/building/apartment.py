from .room import room_area, room_heat


def apartment_area(rooms):
    return sum(room_area(l, w) for l, w in rooms)


def apartment_heat(rooms):
    return sum(room_heat(room_area(l, w)) for l, w in rooms)