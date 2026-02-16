from typing import List, Optional


def water_plants(plant_list: List[Optional[str]]) -> None:
    """Water plants with guaranteed cleanup via finally block."""
    print("Opening watering system")
    try:
        for _ in plant_list:
            if _ is None:
                raise TypeError("Cannot water None - invalid plant!")
            print(f"Watering {_}")
    except TypeError as error:
        print(f"Error; {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Demonstrate finally block with normal and error cases."""
    print("=== Garden Watering System ===")
    print("\nTesting normal watering...")

    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
