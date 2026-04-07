#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:59:32 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/07 18:44:22 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    def __init__(self, name: str, height: float,
                 days: int, growth: float = 1.0) -> None:

        self.name: str = name
        self._height: float = height
        self._days: int = days
        self._growth_rate: float = growth

    def __str__(self) -> str:

        return f"{self.name}: {self._height:.1f}cm, {self._days} days old"

    def get_height(self) -> float:

        return self._height

    def get_age(self) -> int:

        return self._days

    def get_growth_rate(self) -> float:

        return self._growth_rate

    def set_height(self, cm: int) -> None:

        if cm < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = cm
            print(f"Height updated: {self._height}cm")

    def set_age(self, daysip: int) -> None:

        if daysip < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._days = daysip
            print(f"Age updated: {self._days} days")

    def set_growth_rate(self, cms: int) -> None:

        if cms < 0:
            print(f"{self.name}: Error, growth rate can't be negative")
            print("Growth rate update rejected")
        else:
            self._growth_rate = cms
            print(f"Growth rate updated: {cms}cm")

    def grow(self) -> None:

        self._height += self.growth_rate

    def age(self) -> None:

        self._days += 1

    def show(self) -> None:
        print(f"{self.__str__()}")


class Flower(Plant):

    def __init__(
        self, name: str, height: float, age: int, color: str
    ) -> None:

        super().__init__(name, height, age)
        self._color: str = color

    def bloom(self) -> None:

        print(f"{self.name} ({self._color}) is blooming beautifully!\n")


class Tree(Plant):

    def __init__(
        self, name: str, height: float, age: int, diameter: int
    ) -> None:

        super().__init__(name, height, age)
        self._trunk_diameter: int = diameter

    def produce_shade(self) -> None:

        shade: float = self._trunk_diameter * self._height
        print(f"{self.name} provides {shade} square meters of shade\n")


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        season: str,
        nutrition: str
    ) -> None:

        super().__init__(name, height, age)
        self.harvest_season: str = season
        self.nutritional_value: str = nutrition

    def harvest_info(self) -> None:

        print(
            f"{self.name} ({self.harvest_season} harvest"
            f" is rich in {self.nutritional_value})\n"
        )


def main() -> None:

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
