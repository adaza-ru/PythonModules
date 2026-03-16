#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:36:55 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/16 19:02:35 by adaza-ru           ###   ########.fr      #
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

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the Plant with its specific data."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        """Return a user-friendly string representation of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self, cm: int) -> None:
        """Increase the height of the plant."""
        self.height += cm

    def days(self) -> None:
        """Increase the age of the plant by one day."""
        self.age += 1


def main() -> None:
    """Streamlines plant creation by iterating over a data source."""
    raw_data: list[dict] = [
        {"name": "Rose", "height": 25, "age": 30},
        {"name": "Oak", "height": 200, "age": 365},
        {"name": "Cactus", "height": 5, "age": 90},
        {"name": "Sunflower", "height": 80, "age": 45},
        {"name": "Fern", "height": 15, "age": 120}
    ]

    print("=== Plant Factory Output ===")

    for d in raw_data:
        new_plant: Plant = Plant(**d)
        print(new_plant.get_info())

    print("\nTotal plants created: 5")


if __name__ == "__main__":
    main()
