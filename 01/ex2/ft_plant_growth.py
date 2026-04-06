#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:05:25 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/31 15:56:10 by adaza-ru           ###   ########.fr      #
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
        return f"{self.name}: {round(self.height, 1)}cm, {self.days} days old"

    def grow(self) -> None:
        """Increase the height of the plant."""
        self.height += self.growth_rate

    def age(self) -> None:
        """Increase the age of the plant by one day."""
        self.days += 1


def simulate_week(plant: Plant) -> None:
    """Simulates growth for N plants and shows individual results."""
    initial_height: float = plant.height

    print("=== Garden Plant Growth ===")
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        print(plant)
        plant.grow()
        plant.age()
    diff: float = plant.height - initial_height
    print(f"Growth for {plant.name} this week: {round(diff)}cm\n")


def main() -> None:
    """Main execution entry point."""
    plant: Plant = Plant("Rose", 25.0, 0.8, 30)

    simulate_week(plant)


if __name__ == "__main__":
    main()
