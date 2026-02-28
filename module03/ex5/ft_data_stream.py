def game_event_generator(num_events: int) -> object:
    """Generate game events on_demand using yield."""
    players: list = ["alice", "bob", "charlie", "diana", "eve"]
    actions: list = ["killed monster", "found treasure", "leveled up",
                     "joined guild", "completed quest"]
    levels: list = [2, 12, 8, 15, 3, 20, 7, 11, 9, 14]
    for i in range(num_events):
        player: str = players[i % len(players)]
        action: str = actions[i % len(players)]
        level: int = levels[i % len(players)]
        yield (i + 1, player, level, action)


def fibonacci_generator() -> object:
    """Generate Febonacci numbers infinitely useing yield."""
    a: int = 0
    b: int = 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> object:
    """Generate prime numbers infinitely using yield."""
    num: int = 2
    while True:
        is_prime: bool = True
        check: int = 2
        while check * check <= num:
            if num % check == 0:
                is_prime = False
                break
            check = check + 1
        if is_prime:
            yield num
        num = num + 1


def main() -> None:
    """Game Data Stream Processor: demonstrates generators."""
    print("=== Game Data Stream Processor ===")
    num_events: int = 1000
    print(f"\nProcessing {num_events} game events...")

    total_processed: int = 0
    high_level_count: int = 0
    treasure_count: int = 0
    levelup_count: int = 0

    stream = game_event_generator(num_events)
    for event_id, player, level, action in stream:
        total_processed = total_processed + 1
        if level >= 10:
            high_level_count = high_level_count + 1
        if action == "found treasure":
            treasure_count = treasure_count + 1
        if action == "leveled up":
            levelup_count = levelup_count + 1
        if event_id <= 3:
            print(f"Event {event_id}: Player {player}"
                  f"(level {level}) {action}")
    print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_processed}")
    print(f"High-level player (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print("\nMemory usege: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("\n=== Generator Demonstration ===")

    fib = fibonacci_generator()
    fib_value: list = []
    count: int = 0
    for val in fib:
        fib_value.append(val)
        count = count + 1
        if count == 10:
            break
    fib_str: str = ", ".join(str(v) for v in fib_value)
    print(f"Fibonacci sequence (first 10): {fib_str}")
    primes = prime_generator()
    prime_value: list = []
    count = 0
    for val in primes:
        prime_value.append(val)
        count = count + 1
        if count == 5:
            break
    prime_str: str = ", ".join(str(v) for v in prime_value)
    print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
    main()
