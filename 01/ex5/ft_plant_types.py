#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:59:32 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/04 01:20:44 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """Base class for all plants in the garden."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize common plant attributes."""
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_base_info(self) -> str:
        """Return the common info shared by all plants."""
        return f"{self.name}: {self.height}cm, {self.age} days"


class Flower(Plant):
    """Specialized plant type for flowers."""

    def __init__(
        self, name: str, height: int, age: int, color: str
    ) -> None:
        """Use super() to initialize common traits and add color."""
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """Specific behavior for flowers."""
        print(f"{self.name} ({self.color}) is blooming beautifully!\n")


class Tree(Plant):
    """Specialized plant type for trees."""

    def __init__(
        self, name: str, height: int, age: int, diameter: int
    ) -> None:
        """Initialize tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter: int = diameter

    def produce_shade(self, area: int) -> None:
        """Specific behavior for trees."""
        print(f"{self.name} provides {area} square meters of shade\n")


class Vegetable(Plant):
    """Specialized plant type for vegetables."""

    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        season: str,
        nutrition: str
    ) -> None:
        """Initialize vegetable with harvest season and nutrition."""
        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = nutrition

    def harvest_info(self) -> None:
        """Specific behavior for vegetables."""
        print(
            f"{self.name} ({self.harvest_season} harvest"
            f" is rich in {self.nutritional_value})\n"
        )


def main() -> None:
    """Demonstrate the plant family tree using at least 2 instances each."""
    print("=== Garden Plant Types ===")

    rose: Flower = Flower("Rose", 25, 30, "red")
    tulip: Flower = Flower("Tulip", 15, 20, "yellow")
    print(f"{rose.get_base_info()}, {rose.color} color")
    rose.bloom()
    print(f"{tulip.get_base_info()}, {tulip.color} color")
    tulip.bloom()

    oak: Tree = Tree("Oak", 500, 1825, 50)
    pine: Tree = Tree("Pine", 300, 1000, 30)
    print(f"{oak.get_base_info()}, {oak.trunk_diameter}cm diameter")
    oak.produce_shade(78)
    print(f"{pine.get_base_info()}, {pine.trunk_diameter}cm diameter")
    pine.produce_shade(45)

    tomato: Vegetable = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot: Vegetable = Vegetable("Carrot", 20, 60, "winter", "vitamin A")
    print(f"{tomato.get_base_info()}, {tomato.harvest_season} harvest")
    tomato.harvest_info()
    print(f"{carrot.get_base_info()}, {carrot.harvest_season} harvest")
    carrot.harvest_info()


if __name__ == "__main__":
    main()
