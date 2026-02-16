class Plant:
    """Base plant with commin features."""

    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """return basic plant info."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Flower plant type with color and blooming behavior."""

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (
            f"{self.name} (Flower): {self.height}cm,"
            f"{self.age} days, {self.color} color"
        )


class Tree(Plant):
    """Tree plant type with trunk diameter and shade behavior."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        """Return a simple shade estimate in square meters."""
        return (self.trunk_diameter * self.trunk_diameter) // 32

    def get_info(self) -> str:
        return (
            f"{self.name} (Tree):{self.height}cm, {self.age} days, "
            f"{self.trunk_diameter}cm diameter"
        )


class Vegetable(Plant):
    """Vegetable plant type with harvest season and nutritional value."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        return (
            f"{self.name} (Vegetable): {self.height}cm, {self.age} days,"
            f"{self.harvest_season} harvest"
        )

    def show_nutrition(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    flowers = [
        Flower("Rose", 25, 30, "red"),
        Flower("Tulip", 20, 25, "yellow"),
    ]

    trees = [
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1460, 35),
    ]

    vegetables = [
        Vegetable("Tomato", 80, 90, "summer", "vitamin C"),
        Vegetable("carrot", 30, 70, "autumn", "beta-carotene"),
    ]

    print("=== Garden Plant Types ===")

    print()
    for flower in flowers:
        print(flower.get_info())
        flower.bloom()
    print()

    for tree in trees:
        print(tree.get_info())
        shade = tree.produce_shade()
        print(f"{tree.name} provides {shade} square meters of shade")
    print()

    for veg in vegetables:
        print(veg.get_info())
        veg.show_nutrition()
