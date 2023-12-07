class Engineer:
    def __init__(self, first_name: str, last_name: str, unique_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.unique_name = unique_name


class Location:
    def __init__(self, distance_km: float, name: str):
        self.distance_km = distance_km
        self.name = name

    def __str__(self):
        return self.name

    def get_distance_another_location(self, location) -> float:
        difference = self.distance_km - location.distance_km
        return abs(difference)


class LocationEngineer(Location):
    def __init__(self, distance_km: int, name: str, engineer: Engineer):
        super().__init__(distance_km, name)
        self.engineer = engineer


class LocationClient(Location):

    engineer_visit: Engineer = None
