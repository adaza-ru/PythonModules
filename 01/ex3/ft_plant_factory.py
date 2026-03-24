#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:36:55 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/24 19:13:35 by adaza-ru           ###   ########.fr      #
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
                 growth: float, days: int) -> None:
        """Initialize the Plant with its specific data."""
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth

    def __str__(self) -> str:
        """Return a user-friendly string representation of the plant."""
        return f"{self.name}: {self.height}cm, {self.age} days old"

    def grow(self) -> None:
        """Increase the height of the plant."""
        self.height += self.growth_rate

    def age(self) -> None:
        """Increase the age of the plant by one day."""
        self.days += 1


def main() -> None:
    """Streamlines plant creation by iterating over a data source."""
    
    plants: list[list[]] = ["Rose", "Oak", "Cactus", "Sunflower", "Fern",]
	heights: list[float] = [25.0, 200.0, 5.0, 80.0, 15.0]
	ages: list[int] = [30, 365, 90, 45, 120]
    

    print("=== Plant Factory Output ===")

    for d in raw_data:
        new_plant: Plant = Plant(**d)
        print(new_plant.get_info())

    print("\nTotal plants created: 5")


if __name__ == "__main__":
    main()
