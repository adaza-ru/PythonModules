#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/03 22:44:04 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/31 16:31:45 by adaza-ru           ###   ########.fr      #
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


def display_garden(plants: list[Plant]) -> None:
    """
    Prints the registry of all plants in the garden.

    Args:
        plants (list): A variable-size collection containing Plant objects.
    """
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(plant)


def main() -> None:
    """Main execution function to manage garden data."""
    raw_data: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    display_garden(raw_data)


if __name__ == "__main__":
    main()
