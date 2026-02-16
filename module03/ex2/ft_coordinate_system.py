import math


def create_position(x: int, y: int, z: int) -> tuple:
    """Create a 3D position tuple."""
    return (x, y, z)


def calculate_distance(pos1: tuple, pos2: tuple,) -> float:
    """Calculate 3D Euclidean distance between two positions."""
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_str: str) -> tuple:
    """Parse a comma-separated string into a 3D coordinate tuple."""
    parts = coord_str.split(",")
    x: int = int(parts[0])
    y: int = int(parts[1])
    z: int = int(parts[2])
    return (x, y, z)


def main() -> None:
    """Game Coordinate System: demonstrates tuples for 3D positions."""
    print("=== Game Coordinate System ===")
    position: tuple = create_position(10, 20, 5)
    print(f"\nPosition created: {position}")
    origin: tuple = (0, 0, 0)
    dist: float = calculate_distance(origin, position)
    print(
        f"Distance between {origin} and {position}: {round(dist, 2)}"
    )
    valid_str: str = "3,4,0"
    print(f"\nParsing coordinates: \"{valid_str}\"")
    try:
        parsed: tuple = parse_coordinates(valid_str)
        print(f"Parsed position: {parsed}")
        dist2: float = calculate_distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: "
              f"{round(dist2, 2)}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, "
              f"Args: {e.args}")

    invalid_str: str = "abc,def,ghi"
    print(f"\nParsing invalid coordinates: \"{invalid_str}\"")
    try:
        parsed_invalid: tuple = parse_coordinates(invalid_str)
        print(f"Parsed position; {parsed_invalid}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(
            f"Error details - Type: {type(e).__name__}, Args: {e.args}"
        )

    print("\nUnpacking demonstration:")
    x, y, z, = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X{x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
