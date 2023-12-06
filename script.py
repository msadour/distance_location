import random

import pandas as pd

from data.models import LocationClient, LocationEngineer, Engineer
from utils import generate_visits_assigned_as_text


def distance_matrix() -> pd.DataFrame:
    matrix = {}
    locations_engineer = LocationEngineer.objects.all()
    locations_client = LocationClient.objects.all()
    for location_engineer in locations_engineer:
        matrix[location_engineer.name] = [
            location_client.get_distance_another_location(location_engineer)
            for location_client in locations_client
        ]

    df = pd.DataFrame(data=matrix, index=[location_client.name for location_client in locations_client])
    return df


def random_installation_visits() -> str:
    engineers = Engineer.objects.all()

    locations_client_available = [lc for lc in LocationClient.objects.all()]
    random.shuffle(locations_client_available)

    for location_client_available in locations_client_available:
        engineer = engineers.order_by('?').first()
        location_client_available.engineer_visit = engineer

    visits = generate_visits_assigned_as_text(locations_client_available)
    return visits
