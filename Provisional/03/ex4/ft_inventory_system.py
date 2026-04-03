import sys

def main() -> None:
    """Parses inventory data, handles errors, and prints an analysis report."""
    print("=== Inventory System Analysis ===")
    
    inventory: dict[str, int] = {}
    
    for arg in sys.argv[1:]:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'") [cite: 604]
            continue
            
        item, qty_str = arg.split(":", 1)
        
        if item in inventory:
            print(f"Redundant item '{item}' - discarding") [cite: 604]
            continue
            
        try:
            inventory[item] = int(qty_str) [cite: 602]
        except ValueError:
            print(f"Quantity error for '{item}': invalid literal for int()") [cite: 604]
            continue

    if not inventory:
        return

    # Reporting [cite: 603]
    items_list = list(inventory.keys())
    total_qty = sum(inventory.values())
    
    print(f"Got inventory: {inventory}")
    print(f"Item list: {items_list}")
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")
    
    for item, qty in inventory.items():
        pct = (qty / total_qty) * 100
        print(f"Item {item} represents {round(pct, 1)}%")

    # Ties resolved by first occurrence [cite: 603, 604]
    most_abundant = max(inventory, key=lambda k: inventory[k])
    least_abundant = min(inventory, key=lambda k: inventory[k])
    
    print(f"Item most abundant: {most_abundant} with quantity {inventory[most_abundant]}")
    print(f"Item least abundant: {least_abundant} with quantity {inventory[least_abundant]}")
    
    # Add new item [cite: 603]
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")

if __name__ == "__main__":
    main()