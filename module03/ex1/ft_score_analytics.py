import sys


def main() -> None:
    """Score Cruncher: analyzes player scores from command line."""
    print("=== Player Score Analytics ===")
    if len(sys.argv) < 2:
        print(
            "No scores provided. Usege: python3 "
            "ft_score_analytics.py <score1> <score2> ..."
        )
        return
    scores: list = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Warning: '{arg}' is not a valid score, skipping.")
    if len(scores) == 0:
        print("No valid scores to analize.")
        return
    total: int = sum(scores)
    average: float = total / len(scores)
    high: int = max(scores)
    low: int = min(scores)
    score_rang: int = high - low
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_rang}")


if __name__ == "__main__":
    main()
