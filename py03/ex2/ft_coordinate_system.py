import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        position: str = input("Enter new coordinates as "
                              "floats in format 'x,y,z': ")
        splited = position.split(",")
        if len(splited) != 3:
            print("Invalid syntax")
            continue
        co_ord = []
        valid = True
        for split in splited:
            split = split.strip()
            try:
                co_ord.append(float(split))
            except ValueError as error:
                print(f"Error on parameter '{split}': {error}")
                valid = False
                break
        if not valid:
            continue
        return (co_ord[0], co_ord[1], co_ord[2])


def centre_distance(x: float, y: float, z: float) -> float:
    total_distance: float = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    return total_distance


def fXs_distance(first: tuple[float, ...], second: tuple[float, ...]) -> float:
    dx: float = second[0] - first[0]
    dy: float = second[1] - first[1]
    dz: float = second[2] - first[2]
    total_distance: float = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
    return total_distance


def first() -> tuple[float, ...]:
    print("Get a first set of coordinates")
    first: tuple[float, ...] = get_player_pos()
    print(f"Got a first tuple: {first}")
    x: float = first[0]
    y: float = first[1]
    z: float = first[2]
    print(f"It includes: X={x}, Y={y}, Z={z}")
    d_from_c: float = round(centre_distance(x, y, z), 4)
    print(f"Distance to center: {d_from_c}")
    return first


def second(first: tuple[float, ...]) -> None:
    print("Get a second set of coordinates")
    second: tuple[float, float, float] = get_player_pos()
    fXs: float = round(fXs_distance(first, second), 4)
    print(f"Distance between the 2 sets of coordinates: {fXs}")


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    second(first())


if __name__ == "__main__":
    main()
