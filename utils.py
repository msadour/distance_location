def convert_visit_as_text(visits: dict) -> str:
    visits_as_list = [
        f"{engineer} visit {locations}"
        for engineer, locations in visits.items()
    ]
    visits_as_text = ". ".join(visits_as_list)
    return visits_as_text


def calculate_total_km(distances_km: list) -> int:
    total = 0
    for index, distance in enumerate(distances_km):
        if index == 0:
            total += distance
        elif index > 0:
            difference = abs(distance - distances_km[index -1])
            total += difference

    return total
