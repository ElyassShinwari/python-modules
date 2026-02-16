class GardenError(Exception):
    """Base error for all garden-related problems."""

    pass


class PlantError(GardenError):
    """Error for problems with plants."""

    pass


class WaterError(GardenError):
    """Error for problems with watering."""

    pass


class GardenManagement:
    """Garden management system with robust error handling."""

    def __init__(self) -> None:
        """initialize the garden manager."""
        self.plants: dict = {}

    def add_plants(self, name: str) -> None:
        """Add a plant to the garden."""
        if not name:
            raise PlantError("Plant name connot be empty!")
        self.plants[name] = {"water": 0, "sun": 0}
        print(f"Added {name} successfully")

    def water_plants(self) -> None:
        """Water all plantd with guaranteed cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")
        except Exception as e:
            print(f"Error while watering: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, name: str, water: int, sun: int) -> None:
        """Check plant health with validation."""
        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if water < 1:
            raise ValueError(f"Water level {water} is too low (min 1)")
        if sun > 12:
            raise ValueError(f"Sunlight hours {sun} is too high (max 12)")
        if sun < 2:
            raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
        self.plants[name]["water"] = water
        self.plants[name]["sun"] = sun
        print(f"{name}: healthy (water: {water}, sun: {sun})")


def test_garden_management() -> None:
    """Demonstrate all error handling techniques together."""
    print("=== Garden Management System ===")
    garden = GardenManagement()
    print("\nAdding plants to garden...")
    for name in ["tomato", "lettuce", ""]:
        try:
            garden.add_plants(name)
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print("\nWatering plants...")
    garden.water_plants()
    print("\nChecking plant health...")
    health_checks = [
        ("tomato", 5, 8),
        ("lettuce", 15, 8),
    ]
    for name, water, sun in health_checks:
        try:
            garden.check_health(name, water, sun)
        except ValueError as e:
            print(f"Error checking {name}: {e}")
    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
