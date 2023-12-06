import random

from data.models import LocationClient, Engineer


def convert_visit_as_text(visits: dict) -> str:
    visits_as_list = [
        f"{engineer}> visit {locations}"
        for engineer, locations in visits.items()
    ]
    visits_as_text = ". \n".join(visits_as_list)
    return visits_as_text


def calculate_total_km_travelled(distances_km: list) -> int:
    total = 0
    for index, distance in enumerate(distances_km):
        if index == 0:
            total += distance
        elif index > 0:
            difference = abs(distance - distances_km[index-1])
            total += difference

    return total


def build_random_installation_visits() -> dict:
    engineers = Engineer.objects.all()

    locations_client_available = [lc for lc in LocationClient.objects.all()]
    random.shuffle(locations_client_available)

    for location_client_available in locations_client_available:
        engineer = engineers.order_by('?').first()
        location_client_available.engineer_visit = engineer

    visits = {}
    for location in locations_client_available:
        if location.engineer_visit.unique_name not in visits.keys():
            visits[location.engineer_visit.unique_name] = []
        visits[location.engineer_visit.unique_name].append(location.name)

    return visits
