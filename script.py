import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "distance_location.settings")

import django
django.setup()

import pandas as pd

from data.models import LocationClient, LocationEngineer, Engineer
from utils import convert_visit_as_text, calculate_total_km_travelled, build_random_installation_visits


def distance_matrix() -> dict:
    matrix = {}
    locations_engineer = LocationEngineer.objects.all()
    locations_client = LocationClient.objects.all()
    for location_engineer in locations_engineer:
        matrix[location_engineer.engineer.unique_name] = [
            location_client.get_distance_another_location(location_engineer)
            for location_client in locations_client
        ]

    return matrix


def distance_matrix_to_df(matrix: dict) -> pd.DataFrame:
    locations_client = LocationClient.objects.all()
    df = pd.DataFrame(data=matrix, index=[location_client.name for location_client in locations_client])
    return df


def display_random_installation_visits(visits_client_generated: dict):
    visits = convert_visit_as_text(visits_client_generated)
    print(visits)


def calculate_distance_travelled(engineer_unique_name: str, distances: pd.DataFrame, visits: dict) -> int:
    visits_of_engineer = visits.get(engineer_unique_name)
    df = pd.DataFrame(distances, columns=[engineer_unique_name])
    df = df.filter(items=visits_of_engineer, axis=0)
    distances_in_km = df[engineer_unique_name].values.tolist()

    current_engineer = Engineer.objects.filter(unique_name=engineer_unique_name).first()
    location_engineer = LocationEngineer.objects.filter(engineer=current_engineer).first()

    last_visit_distance_km = distances_in_km[-1]
    distance_between_home_and_last_visit = abs(location_engineer.distance_km - last_visit_distance_km)
    total_km_travelled = calculate_total_km_travelled(distances_in_km)
    total_km_travelled += distance_between_home_and_last_visit
    return total_km_travelled


if __name__ == "__main__":
    print("Exercise A: generate a distance matrix")
    distance_matrix = distance_matrix()
    distance_matrix_df = distance_matrix_to_df(matrix=distance_matrix)
    print(distance_matrix_df)
    print("\n")

    print("Exercise B: generates a random sequence of installation visits for the engineers")
    visits_client_available = build_random_installation_visits()
    display_random_installation_visits(visits_client_generated=visits_client_available)
    print("\n")

    print("Exercise C: calculate the distance travelled by engineers")
    engineers = Engineer.objects.all()
    for engineer in engineers:
        total_km = calculate_distance_travelled(
            engineer_unique_name=engineer.unique_name,
            distances=distance_matrix_df,
            visits=visits_client_available
        )
        print(f"{engineer.unique_name} travelled {total_km}km")
    print("\n")

    print("Exercise D: change the sequences of visits made by the engineers")
    visit_jmuller = visits_client_available.get("jmuller")
    location_to_msadour = visit_jmuller.pop(-1)
    visit_msadour = visits_client_available.get("msadour")
    location_to_jmuller = visit_msadour.pop(0)
    visit_jmuller.insert(0, location_to_jmuller)
    visit_msadour.insert(0, location_to_msadour)
    display_random_installation_visits(visits_client_generated=visits_client_available)
    print("\n")
