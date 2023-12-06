from data.models import LocationClient, LocationEngineer


def distance_matrix() -> dict:
    matrix: dict = {}
    locations_engineer = LocationEngineer.objects.all()
    locations_client = LocationClient.objects.all()
    for location_engineer in locations_engineer:
        matrix[location_engineer.name] = [
            {location_client.name: location_client.display_distance_with_name(location_engineer)}
            for location_client in locations_client
        ]
    return matrix
