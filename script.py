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
            f"{location_client.name} is {location_client.display_distance_with_name(location_engineer)}"
            for location_client in locations_client
        ]

    df = pd.DataFrame(data=matrix)
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
