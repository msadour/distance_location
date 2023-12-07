import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "distance_location.settings")

import django

django.setup()

import pandas as pd

from data.objects import engineers, locations_client, locations_engineer
from utils import (
    build_random_installation_visits,
    calculate_total_km_travelled,
    convert_visit_as_text,
    retrieve_location_engineer_by_unique_name,
)


def distance_matrix() -> dict:
    """Create a distance matrix which show the difference distance between engineer location and client location."""
    matrix = {}
    for location_engineer in locations_engineer:
        matrix[location_engineer.engineer.unique_name] = [
            location_client.get_distance_another_location(location_engineer)
            for location_client in locations_client
        ]

    return matrix


def distance_matrix_to_df(matrix: dict) -> pd.DataFrame:
    """Convert the distance matrix (which is a dictionary) into a DataFrame."""
    df = pd.DataFrame(
        data=matrix,
        index=[location_client.name for location_client in locations_client],
    )
    return df


def reduce_km_travelled_visits(distances: pd.DataFrame, visits: dict) -> dict:
    """Sort distance of a DataFrame in order to avoid go and back between locations, which reduce the distance travelled."""
    visits_updated = {}
    for current_engineer, current_visits in visits.items():
        df = pd.DataFrame(distances, columns=[current_engineer])
        df = df.filter(items=current_visits, axis=0).sort_values(
            [current_engineer], ascending=[True]
        )
        visits_updated.update({current_engineer: df.index.values.tolist()})

    return visits_updated


def display_installation_visits(visits: dict):
    """Convert visits dictionary as readable text."""
    visits = convert_visit_as_text(visits)
    print(visits)


def calculate_distance_travelled(
    engineer_unique_name: str, distances: pd.DataFrame, visits: dict
) -> int:
    """Calculate the total distance travelled of an engineer of his/her client location visits."""
    visits_of_engineer = visits.get(engineer_unique_name)

    df = pd.DataFrame(distances, columns=[engineer_unique_name])
    df = df.filter(items=visits_of_engineer, axis=0)
    distances_in_km = df[engineer_unique_name].values.tolist()

    location_engineer = retrieve_location_engineer_by_unique_name(
        engineer_unique_name=engineer_unique_name
    )

    last_visit_distance_km = distances_in_km[-1]
    distance_between_home_and_last_visit = abs(
        location_engineer.distance_km - last_visit_distance_km
    )
    total_km_travelled = calculate_total_km_travelled(distances_in_km)
    total_km_travelled += distance_between_home_and_last_visit

    return round(total_km_travelled, 2)


if __name__ == "__main__":
    print("\nExercise A: generate a distance matrix (in Km) \n----------------------")
    distance_matrix = distance_matrix()
    distance_matrix_df = distance_matrix_to_df(matrix=distance_matrix)
    print(distance_matrix_df)
    print("\n")

    print(
        "Exercise B: generates a random sequence of installation visits for the engineers \n----------------------"
    )
    visits_client_generated = build_random_installation_visits()
    display_installation_visits(visits=visits_client_generated)
    print("\n")

    print(
        "Exercise C: calculate the distance travelled by engineers \n----------------------"
    )
    for engineer in engineers:
        total_km = calculate_distance_travelled(
            engineer_unique_name=engineer.unique_name,
            distances=distance_matrix_df,
            visits=visits_client_generated,
        )
        print(f"{engineer.unique_name} travelled {total_km}km")
    print("\n")

    print(
        "Exercise D: change the sequences of visits made by the engineers \n----------------------"
    )
    visit_jmuller = visits_client_generated.get("jmuller")
    visit_msadour = visits_client_generated.get("msadour")

    new_visit_for_jmuller = visit_msadour.pop(0)
    visit_jmuller.insert(0, new_visit_for_jmuller)

    new_visit_for_msadour = visit_jmuller.pop(-1)
    visit_msadour.insert(0, new_visit_for_msadour)
    display_installation_visits(visits=visits_client_generated)
    print("\n")

    print(
        "Exercise E: filter the new sequences that reduce the total distance travelled by the engineers \n----------------------"
    )
    visits_client_available_travel_reduced = reduce_km_travelled_visits(
        distances=distance_matrix_df, visits=visits_client_generated
    )
    for engineer in engineers:
        total_km_before = calculate_distance_travelled(
            engineer_unique_name=engineer.unique_name,
            distances=distance_matrix_df,
            visits=visits_client_generated,
        )
        print(f"{engineer.unique_name} travelled {total_km_before}km (before)")
        total_km_after = calculate_distance_travelled(
            engineer_unique_name=engineer.unique_name,
            distances=distance_matrix_df,
            visits=visits_client_available_travel_reduced,
        )
        print(f"{engineer.unique_name} travelled {total_km_after}km (after reduce)")
    print("\n")
