def main() -> None:
    """Game Analytics Dashboard: demonstrates comprehensions."""
    print("=== Game Analytics Dashboard ===")

    players: list = [
        {"name": "alice", "score": 2300, "active": True,
         "achievements": ["first_kill", "level_10",
                          "treasure_hunter", "boss_slayer",
                          "speed_demon"]},
        {"name": "bob", "score": 1800, "active": True,
         "achievements": ["first_kill", "level_10",
                          "collector"]},
        {"name": "charlie", "score": 2150, "active": True,
         "achievements": ["level_10", "treasure_hunter",
                          "boss_slayer", "speed_demon",
                          "perfectionist", "collector",
                          "first_kill"]},
        {"name": "diana", "score": 2050, "active": False,
         "achievements": ["first_kill", "level_10",
                          "boss_slayer", "speed_demon"]},
    ]
    print("\n=== List Comprehension Examples ===")
    high_scorers: list = [p["name"] for p in players
                          if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")
    scores_doubled: list = [p["score"] * 2 for p in players]
    print(f"Scores doubled: {scores_doubled}")
    active_player: list = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active_player}")
    print("\n=== Dict Comprehension Examples")
    player_score: dict = {p["name"]: p["score"] for p in players
                          if p["active"]}
    print(f"Player scores: {player_score}")
    scores: list = [p["score"] for p in players]
    high: int = len([s for s in scores if s > 2000])
    medium: int = len([s for s in scores if 1500 <= s <= 2000])
    low: int = len([s for s in scores if s < 1500])
    score_catagories: dict = {"high": high, "medium": medium, "low": low}
    print(f"Score catagories: {score_catagories}")
    achievement_counts: dict = {p["name"]: len(p["achievements"])
                                for p in players}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players: set = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")
    unique_achievement: set = {a for p in players
                               for a in p["achievements"]}
    print(f"Unique Achievement: {unique_achievement}")
    regions: list = ["north", "east", "central", "north",
                     "east", "central", "north"]
    active_regions: set = {r for r in regions}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players: int = len(unique_players)
    print(f"Total players: {total_players}")

    total_achievements: int = len(unique_achievement)
    print(f"Total unique achievements: {total_achievements}")

    avg_score: float = sum(scores) / len(scores)
    print(f"Average score: {avg_score}")

    top: dict = players[0]
    for palyer in players:
        if palyer["score"] > top["score"]:
            top = palyer
    print(f"Top performer: {top['name']}"
          f"({top['score']} points, "
          f"{len(top['achievements'])} achievements)")


if __name__ == "__main__":
    main()
