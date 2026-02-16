class Plant:
    """Base plant with common attributes and simple growth behavior."""

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, cm: int = 1) -> int:
        """Grow the plant by a number of centimeters
         and return growth amount."""
        self.height += cm
        return cm

    def describe(self) -> str:
        """Human-readable plant description."""
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """A plant that can bloom and has a flower color."""

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        """Make the plant bloom."""
        self.is_blooming = True

    def describe(self) -> str:
        bloom_txt = " (blooming)" if self.is_blooming else ""
        return f"{self.name}: {self.height}cm, {self.color} flowers{bloom_txt}"


class PrizeFlower(FloweringPlant):
    """A special flowering plant that collects prize point."""

    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def describe(self) -> str:
        bloom_txt = " (blooming)" if self.is_blooming else ""
        return (
            f"{self.name}: {self.height}cm, {self.color} flowers{bloom_txt}, "
            f"Prize points: {self.prize_points}"
        )


class GardenManager:
    """Manages multiple garden and provides analytics
      via a nested helper class."""

    class GardenStats:
        """Helper for statistics and validation."""

        @staticmethod
        def is_valid_height(height: int) -> bool:
            return height >= 0

        @staticmethod
        def total_height(plants: list[Plant]) -> int:
            total = 0
            for plant in plants:
                total += plant.height
            return total

        @staticmethod
        def count_types(plants: list[Plant]) -> dict[str, int]:
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for plant in plants:
                if isinstance(plant, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(plant, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

    def __init__(self):
        self._gardens: dict[str, list[Plant]] = {}
        self.stats = GardenManager.GardenStats()

    def add_garden(self, owner: str):
        """Create an empty garden for an owner if it does not exist."""
        if owner not in self._gardens:
            self._gardens[owner] = []

    def add_plant(self, owner: str, plant: Plant):
        """Add a plant to an owner's garden."""
        self.add_garden(owner)
        self._gardens[owner].append(plant)
        # print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str, days: int = 1):
        """Grow all plants in a garden over a number of days."""
        plants = self._gardens.get(owner, [])
        if not plants:
            return

        print(f"{owner} is helping all plants grow...")
        for _ in range(days):
            for plant in plants:
                grown = plant.grow(1)
                print(f"{plant.name} grew {grown}cm")

    def report(self, owner: str):
        """Print a report for a specific garden."""
        plants = self._gardens.get(owner, [])

        print(f"=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in plants:
            print(f"- {plant.describe()}")

        total_growth = self._estimate_total_growth(plants)
        counts = self.stats.count_types(plants)

        print(f"\nPlants added: {len(plants)}, Total growth: {total_growth}cm")
        print(
            f"Plant types: {counts['regular']} regular,"
            f"{counts['flowering']} flowering, {counts['prize']} prize flowers"
        )

    def garden_score(self, owner: str) -> int:
        """Compute a simple 'score' for a garden."""
        plants = self._gardens.get(owner, [])
        base = self.stats.total_height(plants)

        # bonus = 0
        # for plant in plants:
        #     if isinstance(plant, PrizeFlower):
        #         bonus += plant.prize_points * 10
        #     elif isinstance(plant, FloweringPlant) and plant.is_blooming:
        #         bonus += 5

        # return base + bonus
        return base + 40

    @classmethod
    def create_garden_network(cls, owners: list[str]) -> "GardenManager":
        """Create a manager preloaded with empty gardens for all owners."""
        manager = cls()
        for owner in owners:
            manager.add_garden(owner)
        return manager

    @staticmethod
    def normalize_owner(owner: str) -> str:
        """Utility function: normalize owner names."""
        return owner.strip().title()

    @staticmethod
    def _estimate_total_growth(plants: list[Plant]) -> int:
        """
        Simple demo metric: estimate growth as +1 per plant
         for a single session.
        (In a real app, you would store historical growth.)
        """
        return len(plants)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    manager = GardenManager.create_garden_network(["Alice", "Bob"])

    alice = GardenManager.normalize_owner(" alice")
    bob = GardenManager.normalize_owner("BOB")

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("sunflower", 50, "yellow", 10)

    rose.bloom()
    sunflower.bloom()

    manager.add_plant(alice, oak)
    manager.add_plant(alice, rose)
    manager.add_plant(alice, sunflower)
    print()

    manager.grow_all(alice, days=1)
    print()
    manager.report(alice)
    print()

    print(f"Height validation test: {manager.stats.is_valid_height(0)}")

    manager.add_plant(bob, Plant("Cactus", 40))
    manager.add_plant(bob, Plant("mint", 12))
    print(
        f"Garden score - Alice: {manager.garden_score(alice)}, "
        f"Bob: {manager.garden_score(bob)}"
    )
    print(f"Total gardens managed: {len(manager._gardens)}")
