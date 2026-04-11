#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_types.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:59:32 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/08 19:49:06 by adaza-ru           ###   ########.fr      #
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

    def set_height(self, cm: float) -> None:

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

    def grow(self, times: int | None = None) -> None:

        self._height += (
            self._growth_rate if times is None else self._growth_rate * times
        )

    def age(self, days: int = 1) -> None:

        self._days += days

    def show(self) -> None:
        print(f"{self.__str__()}")


class Flower(Plant):

    def __init__(
        self, name: str, height: float, age: int,
        color: str, growth: float = 1.0
    ) -> None:

        super().__init__(name, height, age, growth)
        self._color: str = color
        self.blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self.blooming is False:
            print(" Rose has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")

    def bloom(self) -> None:

        if self.blooming is False:
            self.blooming = True


class Tree(Plant):

    def __init__(
        self, name: str, height: float, age: int,
        diameter: float, growth: float = 1.0
    ) -> None:

        super().__init__(name, height, age, growth)
        self._trunk_diameter: float = diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        growth: float = 1.0
    ) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def grow(self, times: int | None = None) -> None:
        super().grow(times)
        self.nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def main() -> None:

    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose: Flower = Flower("Rose", 15, 10, "red")
    rose.show()
    print(f"[asking the {rose.name} to bloom]")
    rose.bloom()
    rose.show()

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()

    print("\n=== Vegetable")
    tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April", growth=2.1)
    tomato.show()
    print(f"[make the {tomato.name} grow and age for 20 days]")
    tomato.grow(20)
    tomato.age(20)
    tomato.show()


if __name__ == "__main__":
    main()
