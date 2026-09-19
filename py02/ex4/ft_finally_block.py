
class GardenError(Exception):
    def __init__(self, message: str = "unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "unknown plant error") -> None:
        super().__init__(message)

def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


if __name__ == "__main__":
    water_plant("hello")
    print()
    water_plant("Hello")