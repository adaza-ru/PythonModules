#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:05:25 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/08 16:28:19 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float,
                 growth: float, days: int) -> None:

        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth

    def __str__(self) -> str:

        return f"{self.name}: {round(self.height, 1)}cm, {self.days} days old"

    def grow(self, times: int | None = None) -> None:

        self.height += (
            self.growth_rate if times is None else self.growth_rate * times
        )

    def age(self, days: int = 1) -> None:

        self.days += days

    def show(self) -> None:
        print(f"{self.__str__()}")


def simulate_week(plant: Plant) -> None:

    initial_height: float = plant.height

    print("=== Garden Plant Growth ===")
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant.show()
        plant.grow()
        plant.age()

    diff: float = plant.height - initial_height
    print(f"Growth this week: {round(diff, 1)}cm\n")


def main() -> None:

    plant: Plant = Plant("Rose", 25.0, 0.8, 30)

    simulate_week(plant)


if __name__ == "__main__":
    main()
