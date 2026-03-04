#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:36:55 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/04 01:16:13 by adaza-ru           ###   ########.fr      #
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


def main() -> None:
    """Streamlines plant creation by iterating over a data source."""
    raw_data: tuple = (
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120),
    )

    print("=== Plant Factory Output ===")

    for i in range(5):
        name, height, age = raw_data[i]
        new_plant: Plant = Plant(name, height, age)

        print(new_plant.get_info())

    print("\nTotal plants created: 5")


if __name__ == "__main__":
    main()
