import sys


def main() -> None:
    """Parses inventory data, handles errors, and prints an analysis report."""

    if len(sys.argv) == 1:
        print("Usage: python3 ft_inventory_system.py <item1:quantity>"
              " <item2:quantity> ...")
        return

    print("=== Inventory System Analysis ===")

    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        item: str
        qty_str: str
        item, qty_str = arg.split(":", 1)

        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            inventory[item] = int(qty_str)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue

    if not inventory:
        print("Wrong inventory. Usage: python3 ft_inventory_system.py "
              "<item1:quantity> <item2:quantity> ...")
        return

    items_list: list[str] = list(inventory.keys())
    total_qty: int = sum(inventory.values())

    print(f"Got inventory: {inventory}")
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        pct: float = (qty / total_qty) * 100
        print(f"Item {item} represents {round(pct, 1)}%")

    most_abundant: str = ""
    least_abundant: str = ""

    if items_list:
        most_abundant = items_list[0]
        least_abundant = items_list[0]

    for item in inventory:
        if inventory[item] > inventory[most_abundant]:
            most_abundant = item

        if inventory[item] < inventory[least_abundant]:
            least_abundant = item

    print(f"Item most abundant: {most_abundant} ", end="")
    print(f"with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} ", end="")
    print(f"with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
