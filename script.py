import random

import pandas as pd

from data.models import LocationClient, LocationEngineer, Engineer
from utils import convert_visit_as_text, calculate_total_km


def distance_matrix() -> pd.DataFrame:
    matrix = {}
    locations_engineer = LocationEngineer.objects.all()
    locations_client = LocationClient.objects.all()
    for location_engineer in locations_engineer:
        matrix[location_engineer.engineer.full_name()] = [
            location_client.get_distance_another_location(location_engineer)
            for location_client in locations_client
        ]

    df = pd.DataFrame(data=matrix, index=[location_client.name for location_client in locations_client])
    return df


def build_random_installation_visits() -> dict:
    engineers = Engineer.objects.all()

    locations_client_available = [lc for lc in LocationClient.objects.all()]
    random.shuffle(locations_client_available)

    for location_client_available in locations_client_available:
        engineer = engineers.order_by('?').first()
        location_client_available.engineer_visit = engineer

    visits = {}
    for location in locations_client_available:
        if location.engineer_visit.full_name() not in visits.keys():
            visits[location.engineer_visit.full_name()] = []
        visits[location.engineer_visit.full_name()].append(location.name)

    return visits


def display_random_installation_visits() -> str:
    locations_client_available = build_random_installation_visits()
    visits = convert_visit_as_text(locations_client_available)
    return visits


def calculate_distance_travelled(engineer_name: str) -> int:
    distances = distance_matrix()
    visits = build_random_installation_visits()
    visits_of_engineer = visits.get(engineer_name)
    df = pd.DataFrame(distances, columns=[engineer_name])
    df = df.filter(items=visits_of_engineer, axis=0)
    distances_in_km = df[engineer_name].values.tolist()
    total_km = calculate_total_km(distances_in_km)
    return total_km
