#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:05:25 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/04 00:34:49 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """
    A class used to represent a community garden plant.

    Attributes:
        name (str): The common name of the plant.
        height (int): The height of the plant in centimeters.
        days (int): The days of the plant in days.
    """

    def __init__(self, name: str, height: int, days: int) -> None:
        """Initialize the Plant with its specific data."""
        self.name: str = name
        self.height: int = height
        self.days: int = days

    def get_info(self) -> str:
        """Return a user-friendly string representation of the plant."""
        return f"{self.name}: {self.height}cm, {self.days} days old"

    def grow(self, cm: int) -> None:
        """Increase the height of the plant."""
        self.height += cm

    def age(self) -> None:
        """Increase the age of the plant by one day."""
        self.days += 1


def simulate_week(plants: tuple, num_plants: int) -> None:
    """Simulates growth for N plants and shows individual results."""
    initial_heights = [0] * num_plants
    for i in range(num_plants):
        initial_heights[i] = plants[i].height

    print("=== Day 1 ===")
    for i in range(num_plants):
        print(plants[i].get_info())

    for _ in range(6):
        for i in range(num_plants):
            plants[i].grow(1)
            plants[i].age()

    print("\n=== Day 7 ===")
    for i in range(num_plants):
        print(plants[i].get_info())
        diff = plants[i].height - initial_heights[i]
        print(f"Growth for {plants[i].name}: +{diff} cm")


def main() -> None:
    """Main execution entry point."""
    rose: Plant = Plant("Rose", 25, 30)
    garden: tuple = (rose,)

    simulate_week(garden, 1)


if __name__ == "__main__":
    main()
