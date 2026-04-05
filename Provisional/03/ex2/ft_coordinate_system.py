import math


def get_player_pos() -> tuple[float, float, float]:
    """
    Repeatedly prompts the user for 3D coordinates
    until a valid format is given.
    Returns:
        tuple: (x, y, z) as floats.
    """
    while True:
        try:
            user_input: str = input("Enter new coordinates as"
                                    " floats in format 'x,y,z': ")
            parts: list[str] = [p.strip() for p in user_input.split(',')]

            if len(parts) != 3:
                print("Invalid syntax")
                continue

            return (float(parts[0]), float(parts[1]), float(parts[2]))
        except ValueError as e:
            error_val: str = e.__str__().split(':')[-1].strip()
            print(f"Error on parameter {error_val}: {e}")
            continue


def main() -> None:
    """Orchestrates the coordinate collection and distance calculation."""
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    p1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {p1}")
    print(f"It includes: X={p1[0]}, Y={p1[1]}, Z={p1[2]}")

    dist_to_center: float = math.sqrt(p1[0]**2 + p1[1]**2 + p1[2]**2)
    print(f"Distance to center: {round(dist_to_center, 4)}")

    print("\nGet a second set of coordinates")
    p2: tuple[float, float, float] = get_player_pos()

    dist_between: float = math.sqrt(
        (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2
    )
    print("Distance between the 2 sets of coordinates: ", end="")
    print(f"{round(dist_between, 4)}")


if __name__ == "__main__":
    main()
