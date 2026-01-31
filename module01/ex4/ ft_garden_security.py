class SecurePlant:
    """Plant with protected and validated data."""

    def __init__(self, name: str):
        self.name = name
        self._height = 0
        self._age = 0

    def set_height(self, height: int):
        if height < 0:
            print("Security: Negative height rejected")
            return
        self._height = height
        print(f"Height updated: {self._height}cm [OK]")

    def set_age(self, age: int):
        if age < 0:
            print("Security: Negative age rejected")
            return
        self._age = age
        print(f"Age updated: {self._age} days [OK]")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> str:
        return f"{self.name} ({self._height}cm, {self._age} days)"


if __name__ == "__main__":
    plant = SecurePlant("Rose")

    print("=== Garden Security System ===")
    print("Plant created: Rose")

    plant.set_height(25)
    plant.set_age(30)

    print("\nInvalid operation attempted: height -5cm [REJECTED]")
    plant.set_height(-5)

    print(f"\nCurrent plant: {plant.get_info()}")
