class GardenError(Exception):
    """Base error for all gerdan-related problems."""

    pass


class PlantError(GardenError):
    """Error for problem with plants."""

    pass


class WaterError(GardenError):
    """Error for problem with watering."""

    pass


def check_plant(plant_name: str) -> None:
    """Check the plant and raise PlantError if wilting."""
    if plant_name == "wilting_tomato":
        raise PlantError("The tomato plant is wilting!")


def check_water(water_leve: int) -> None:
    """Check water and raise WaterError if too low."""
    if water_leve < 10:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    """Demonstrate custom garden error types."""
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant("wilting_tomato")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print("\nTasting WaterError...")
    try:
        check_water(5)
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTasting catching all garden errors...")
    errors_to_raise = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!"),
    ]
    for error in errors_to_raise:
        try:
            raise error
        except GardenError as e:
            print(f"Caugth a garden error: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
