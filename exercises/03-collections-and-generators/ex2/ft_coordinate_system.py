import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        user_input: str = input("Enter new coordinates "
                                "as floats in format 'x,y,z': ")
        coords: list[str] = [p.strip() for p in user_input.split(',')]

        if len(coords) != 3:
            print("Invalid syntax")
            continue

        try:
            x: float = float(coords[0])
            y: float = float(coords[1])
            z: float = float(coords[2])
            return (x, y, z)
        except ValueError as e:
            for p in coords:
                try:
                    float(p)
                except ValueError:
                    print(f"Error on parameter '{p}': {e}")
                    break
            continue


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    p1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {p1}")
    x1, y1, z1 = p1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    dist_to_center: float = math.sqrt(x1**2 + y1**2 + z1**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("\nGet a second set of coordinates")
    p2: tuple[float, float, float] = get_player_pos()
    x2, y2, z2 = p2
    dist_between: float = math.sqrt(
        (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
    )
    print("Distance between the 2 sets of coordinates: ", end="")
    print(f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
