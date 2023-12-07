import random
from typing import Optional

from data.models import Engineer, LocationClient, LocationEngineer
from data.objects import engineers, locations_client, locations_engineer


def convert_visit_as_text(visits: dict) -> str:
    visits_as_list = [
        f"{engineer}> visit {locations}" for engineer, locations in visits.items()
    ]
    visits_as_text = ". \n".join(visits_as_list)
    return visits_as_text


def calculate_total_km_travelled(distances_km: list) -> int:
    total = 0
    for index, distance in enumerate(distances_km):
        if index == 0:
            total += distance
        elif index > 0:
            difference = abs(distance - distances_km[index - 1])
            total += difference

    return total


def build_random_installation_visits() -> dict:
    random.shuffle(locations_client)

    for location_client_available in locations_client:
        engineer = random.choice(engineers)
        location_client_available.engineer_visit = engineer

    visits = {}
    for location in locations_client:
        if location.engineer_visit.unique_name not in visits.keys():
            visits[location.engineer_visit.unique_name] = []
        visits[location.engineer_visit.unique_name].append(location.name)

    return visits


def retrieve_engineer_by_unique_name(engineer_unique_name: str) -> Optional[Engineer]:
    for engineer in engineers:
        if engineer.unique_name == engineer_unique_name:
            return engineer

    raise Exception("Engineer doesn't exist")


def retrieve_location_engineer_by_unique_name(
    engineer_unique_name: str,
) -> Optional[LocationEngineer]:
    for location in locations_engineer:
        if location.engineer.unique_name == engineer_unique_name:
            return location

    raise Exception("Location engineer doesn't exist")
