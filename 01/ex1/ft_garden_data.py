#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/03 22:44:04 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/04 00:03:11 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """
    A class used to represent a community garden plant.

    Attributes:
        name (str): The common name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the Plant with its specific data."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        """Return a user-friendly string representation of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"


def display_garden(plants: tuple) -> None:
    """
    Prints the registry of all plants in the garden.

    Args:
        plants (tuple): A fixed-size collection containing Plant objects.
    """
    print("=== Garden Plant Registry ===")
    for i in range(3):
        print(plants[i])


def main() -> None:
    """Main execution function to manage garden data."""
    rose: Plant = Plant("Rose", 25, 30)
    sunflower: Plant = Plant("Sunflower", 80, 45)
    cactus: Plant = Plant("Cactus", 15, 120)

    garden_data: tuple = (rose, sunflower, cactus)

    display_garden(garden_data)


if __name__ == "__main__":
    main()
