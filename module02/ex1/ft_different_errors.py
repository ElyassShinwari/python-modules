def garden_operations() -> None:
    """Demonstrate common error typws in the garden operations."""
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print("\n Testing ZeroDivisionError...")
    try:
        100 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: Division by zero")
    print("\nTesting FileNotFoundError...")
    try:
        f = open("missing.txt", "r")
        f.close()
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print("\nTesting KeyError...")
    try:
        garden = {"tomato": 5, "lettuce": 3}
        garden["_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")


def test_error_types() -> None:
    """Test all error types and demonstrate multiple catch."""
    print("=== Garden Error Type Demo ===\n")
    garden_operations()
    print("\nTesting multiple errors together...")

    def bad_int():
        return int("not a integer")

    def bad_division():
        return 1 / 0

    operations = [bad_int, bad_division]
    for op in operations:
        try:
            op()
        except (ValueError, ZeroDivisionError):
            print("", end="")
    print("Caught some errors, but program continues!")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
