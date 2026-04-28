from ex0.factories import CreatureFactory
from ex0.creatures import Creature
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.capabilities import HealCapability, TransformCapability


def test_healing_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label, creature in [
        (" base:", factory.create_base()),
        (" evolved:", factory.create_evolved()),
    ]:
        print(label)
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform_factory(factory: CreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label, creature in [
        (" base:", factory.create_base()),
        (" evolved:", factory.create_evolved()),
    ]:
        print(label)
        c: Creature = creature
        print(c.describe())
        print(c.attack())
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(c.attack())
            print(creature.revert())


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing_factory(heal_factory)
    print()
    test_transform_factory(transform_factory)
