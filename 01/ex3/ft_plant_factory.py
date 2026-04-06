#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:36:55 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/31 16:27:09 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """
    A class used to represent a community garden plant.

    Attributes:
        name (str): The common name of the plant.
        height (float): The height of the plant in centimeters.
        days (int): The days of the plant in days.
        growth_rate (float): How much the plant grows each day.
    """

    def __init__(self, name: str, height: float,
                 days: int, growth: float = 1.0) -> None:
        """Initialize the Plant with its specific data."""
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth

    def __str__(self) -> str:
        """Return a user-friendly string representation of the plant."""
        return f"{self.name}: {round(self.height)}cm, {self.days} days old"

    def grow(self) -> None:
        """Increase the height of the plant."""
        self.height += self.growth_rate

    def age(self) -> None:
        """Increase the age of the plant by one day."""
        self.days += 1


def main() -> None:
    """Streamlines plant creation by iterating over a data source."""

    plants: list[list[str] | list[float] | list[int]] = [
            ["Rose", "Oak", "Cactus", "Sunflower", "Fern",],
            [25.0, 200.0, 5.0, 80.0, 15.0],
            [30, 365, 90, 45, 120]]
    total_plants: int = 0

    print("=== Plant Factory Output ===")
    for n, h, d in zip(*plants):
        new_plant: Plant = Plant(n, h, d)
        print(new_plant)
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")


if __name__ == "__main__":
    main()
