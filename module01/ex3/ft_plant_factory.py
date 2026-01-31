class Plant:
    """Represents a plant with basic garden information."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"{self.name} ({self.height}cm, {self.age} days)"


def create_plants() -> list[Plant]:
    """Create and return a list of plants with different starting values."""
    return [
          Plant("Rose", 25, 30),
          Plant("Oak", 200, 365),
          Plant("Cactus", 5, 90),
          Plant("Sunflower", 80, 45),
          Plant("Fern", 15, 120),
     ]


if __name__ == "__main__":
    plants = create_plants()

    print("== Plant Factory Output ===")
    for p in plants:
        print(f"Created: {p.get_info()}")

    print(f"\nTotal plants created: {len(plants)}")
