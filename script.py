from data.models import Location


def distance_matrix(location_name: str = None) -> dict:
    matrix: dict = {}

    if location_name:
        location = Location.objects.filter(name=location_name).first()
        other_locations = Location.objects.all().exclude(id=location.id)
        matrix[location.name] = [
            {other_location.name: other_location.get_distance_another_location(location)}
            for other_location in other_locations
        ]
        return matrix

    all_locations = Location.objects.all()
    for location in all_locations:
        other_locations = Location.objects.all().exclude(id=location.id)
        matrix[location.name] = [
            {other_location.name: other_location.get_distance_another_location(location)}
            for other_location in other_locations
        ]

    return matrix
