import sys
import math


def get_player_pos() -> tuple:
    while True:
        position: str = input("Enter new coordinates as floats in format 'x,y,z': ")
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
        if not valid:
            continue
        return (co_ord[0] ,co_ord[1], co_ord[2])


def find_distance(x: float,y: float,z: float,) -> float:
    total_distance: float = math.sqrt(x ** 2 + y ** 2 + z ** 2)
    return total_distance
    

def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    coordinate : tuple = get_player_pos()
    print(f"Got a first tuple: {coordinate}")
    x: float = coordinate[0]
    y: float = coordinate[1]
    z: float = coordinate[2]
    print(f"It includes: X = {x}, Y = {y}, Z = {z}")
    d_from_c : float = round(find_distance(x,y,z), 4)
    print(f"Distance to center: {d_from_c}")
if __name__ == "__main__":
    main()
