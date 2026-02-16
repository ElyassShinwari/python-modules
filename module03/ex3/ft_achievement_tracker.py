def main() -> None:
    """Achievement Tracker: demonstrates set operations."""
    print("=== Achievement Tracker System ===")
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {
        "level_10",
        "treasure_hunter",
        "boss_slayer",
        "speed_demon",
        "perfectionist",
    }
    print(f"\nPlayer alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achivement Analytics ===")
    all_achivements: set = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achivements}")
    print(f"Total unique achievements: {len(all_achivements)}")

    common = alice.intersection(bob).intersection(charlie)
    print(f"\nCommon to all players: {common}")
    rare: set = set()
    for achievment in all_achivements:
        count = 0

        if achievment in alice:
            count = count + 1
        if achievment in bob:
            count = count + 1
        if achievment in charlie:
            count = count + 1

        if count == 1:
            rare.add(achievment)
    print(f"Rare achievements (1 player): {rare}")
    alice_vs_bob_common: set = alice.intersection(bob)
    print(f"\nAlice vs Bob common: {alice_vs_bob_common}")
    alice_unique: set = alice.difference(bob)
    print(f"Alice unique: {alice_unique}")
    bob_unique: set = bob.difference(alice)
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
