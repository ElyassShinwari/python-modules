class Plant:
    """Represents a plant in the garden."""

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
        """Increase plant height by 1 cm."""
        self.height += 1

    def age_one_day(self):
        """Increase plant age by 1 day."""
        self.age += 1

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


if __name__ == "__main__":
    plant = Plant("rose", 25, 30)

    print("=== Day 1 ===")
    print(plant.get_info())

    for _ in range(6):
        plant.grow()
        plant.age_one_day()

    print("=== Day 7 ===")
    print(plant.get_info())
    print("Growth this week: +6cm")
