import sys


def main() -> None:
    """Inventory System: manages game inventory with dictionaries."""
    print("=== Inventory System Analysis ===")

    if len(sys.argv) < 2:
        print(
            "No Items provided. Usege: Python3 "
            "ft_inventory_system.py item:qty item:qty ..."
        )
        return

    inventory: dict = {}
    for arg in sys.argv[1:]:
        try:
            parts = arg.split(":")
            name: str = parts[0]
            qty: int = int(parts[1])
            inventory[name] = inventory.get(name, 0) + qty
        except (ValueError, IndexError):
            print(f"Warning: '{arg}' is not valid, skipping.")

    if len(inventory) == 0:
        print("No valid items to analyze.")
        return

    total_items: int = sum(inventory.values())
    unique_types: int = len(inventory)
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print("\n=== Current Inventory ===")

    def get_qty(item):
        return item[1]

    sorted_items: list = sorted(inventory.items(), key=get_qty, reverse=True)
    for name, qty in sorted_items:
        pct: float = round(qty / total_items * 100, 1)
        unit: str = "unit" if qty == 1 else "units"
        print(f"{name}: {qty} {unit} ({pct}%)")

    print("=== Inventory Statistics ===")
    most_name: str = max(inventory, key=inventory.get)
    least_name: str = min(inventory, key=inventory.get)
    print(f"Most abundant: {most_name} " f"({inventory[most_name]} units)")
    print(f"Least abundant: {least_name} " f"({inventory[least_name]} units)")

    print("\n=== Item Categories ===")
    moderate: dict = {}
    scarce: dict = {}
    for name, qty in inventory.items():
        if qty >= 5:
            moderate[name] = qty
        else:
            scarce[name] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print("\n=== Management Suggestions ===")
    restock: list = []
    for name, qty in inventory.items():
        if qty <= 1:
            restock.append(name)
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {list(inventory.keys())}")
    print(f"Dictionary values: {list(inventory.values())}")
    sample_key: str = list(inventory.keys())[0]
    print(f"Sample lookup - '{sample_key}' in inventory: "
          f"{sample_key in inventory}")


if __name__ == "__main__":
    main()
