from data.models import LocationClient


def generate_visits_assigned_as_text(locations_client: list[LocationClient]):
    visits = {}
    for location in locations_client:
        if location.engineer_visit.full_name() not in visits.keys():
            visits[location.engineer_visit.full_name()] = []
        visits[location.engineer_visit.full_name()].append(location.name)

    visits_as_list = [
        f"{engineer} visit {locations}"
        for engineer, locations in visits.items()
    ]
    visits_as_text = ". ".join(visits_as_list)
    return visits_as_text
