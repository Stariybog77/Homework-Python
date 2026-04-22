from .apartment import apartment_area, apartment_heat


def building_area(apartments):
    return sum(apartment_area(a) for a in apartments)


def building_heat(apartments):
    return sum(apartment_heat(a) for a in apartments)