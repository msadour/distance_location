import random

from .models import Engineer, LocationClient, LocationEngineer

engineer_1 = Engineer(first_name="Mehdi", last_name="Sadour", unique_name="msadour")
engineer_2 = Engineer(first_name="Joe", last_name="Muller", unique_name="jmuller")

location_client_A = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client A"
)
location_client_B = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client B"
)
location_client_C = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client C"
)
location_client_D = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client D"
)
location_client_E = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client E"
)
location_client_F = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client F"
)
location_client_G = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client G"
)
location_client_H = LocationClient(
    distance_km=round(random.uniform(1.0, 50.0), 1), name="Location client H"
)

location_engineer_1 = LocationEngineer(
    distance_km=0, name="Location engineer Mehdi", engineer=engineer_1
)
location_engineer_2 = LocationEngineer(
    distance_km=10, name="Location engineer Joe", engineer=engineer_2
)

locations_client = [
    location_client_A,
    location_client_B,
    location_client_C,
    location_client_D,
    location_client_E,
    location_client_F,
    location_client_G,
    location_client_H,
]

locations_engineer = [
    location_engineer_1,
    location_engineer_2,
]

engineers = [engineer_1, engineer_2]
