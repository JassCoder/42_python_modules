import sys


def parse_inventory(argv: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in argv:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, value = arg.split(':', 1)
        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue
        try:
            inventory[name] = int(value)
        except ValueError as e:
            print(f"Quantity error for '{name}': {e}")

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")

    if not inventory:
        print("At the beginning of the game, "
              "your inventory is usually empty ;)")
        return

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total: int = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")

    for name in items:
        pct: float = round(inventory[name] / total * 100, 1)
        print(f"Item {name} represents {pct}%")

    most: str = items[0]
    least: str = items[0]
    for name in items:
        if inventory[name] > inventory[most]:
            most = name
        if inventory[name] < inventory[least]:
            least = name

    print(f"Item most abundant: {most} with quantity {inventory[most]}")
    print(f"Item least abundant: {least} with quantity {inventory[least]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
