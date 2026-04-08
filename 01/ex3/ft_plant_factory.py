#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_factory.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:36:55 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/08 15:45:17 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float,
                 days: int, growth: float = 1.0) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.growth_rate: float = growth

    def __str__(self) -> str:

        return f"{self.name}: {round(self.height, 1)}cm, {self.days} days old"

    def grow(self) -> None:

        self.height += self.growth_rate

    def age(self) -> None:

        self.days += 1

    def show(self) -> None:
        print(f"{self.__str__()}")


def main() -> None:

    plants: list[list[str] | list[float] | list[int]] = [
            ["Rose", "Oak", "Cactus", "Sunflower", "Fern",],
            [25.0, 200.0, 5.0, 80.0, 15.0],
            [30, 365, 90, 45, 120]]
    total_plants: int = 0

    print("=== Plant Factory Output ===")
    for n, h, d in zip(*plants):
        new_plant: Plant = Plant(n, h, d)
        new_plant.show()
        total_plants += 1
    print(f"\nTotal plants created: {total_plants}")


if __name__ == "__main__":
    main()
