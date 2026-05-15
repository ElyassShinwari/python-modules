from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (spell1(target, power), spell2(target, power))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    def cast(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        return [spell(target, power) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} with {power} armor"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    r1, r2 = combined("Dragon", 10)
    r1_short = r1.split(" for")[0]
    print(f"Combined spell result: {r1_short}, Heals Dragon")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    orig = fireball("Enemy", 10)
    amped = mega_fireball("Enemy", 10)
    orig_power = 10
    amped_power = 30
    print(f"Original: {orig_power}, Amplified: {amped_power}")

    print("\nTesting conditional caster...")
    high_power = conditional_caster(
        lambda t, p: p >= 50, fireball
    )
    print(high_power("Goblin", 60))
    print(high_power("Goblin", 10))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Hero", 20)
    for result in results:
        print(result)
