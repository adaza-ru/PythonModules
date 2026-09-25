#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 01:43:03 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/14 18:23:53 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:

    class _Stats:
        def __init__(self) -> None:
            self._grow_calls: int = 0
            self._age_calls: int = 0
            self._show_calls: int = 0

        def add_grow(self) -> None:
            self._grow_calls += 1

        def add_age(self) -> None:
            self._age_calls += 1

        def add_show(self) -> None:
            self._show_calls += 1

        def display(self) -> None:
            print(
                f"Stats: {self._grow_calls} grow, "
                f"{self._age_calls} age, {self._show_calls} show"
            )

    def __init__(
        self,
        name: str,
        height: float,
        days: int,
        growth: float = 1.0
    ) -> None:
        self.name: str = name
        self._height: float = height
        self._days: int = days
        self._growth_rate: float = growth
        self._stats: Plant._Stats = Plant._Stats()

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

    @staticmethod
    def older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def grow(self, times: int | None = None) -> None:

        self._height += (
            self._growth_rate if times is None else self._growth_rate * times
        )
        self._stats.add_grow()

    def age(self, days: int = 1) -> None:

        self._days += days
        self._stats.add_age()

    def show(self) -> None:
        print(self)
        self._stats.add_show()

    def show_stats(self) -> None:
        self._stats.display()


class Flower(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth: float = 1.0
    ) -> None:
        super().__init__(name, height, age, growth)
        self._color: str = color
        self.blooming: bool = False

    def bloom(self) -> None:
        self.blooming = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self._color}")
        if self.blooming is False:
            print(f" {self.name} has not bloomed yet")
        else:
            print(f" {self.name} is blooming beautifully!")


class Tree(Plant):

    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self.__shade_calls: int = 0

        def add_shade(self) -> None:
            self.__shade_calls += 1

        def display(self) -> None:
            super().display()
            print(f" {self.__shade_calls} shade")

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        diameter: float,
        growth: float = 1.0
    ) -> None:
        super().__init__(name, height, age, growth)
        self._trunk_diameter: float = diameter
        self._stats: Tree._TreeStats = Tree._TreeStats()

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self._trunk_diameter:.1f}cm wide."
        )
        self._stats.add_shade()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self._trunk_diameter:.1f}cm")


class Vegetable(Plant):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        season: str,
        growth: float = 1.0
    ) -> None:
        super().__init__(name, height, age, growth)
        self.harvest_season: str = season
        self.nutritional_value: int = 0

    def grow(self, times: int | None = None) -> None:
        super().grow(times)
        self.nutritional_value += 1

    def age(self, days: int = 1) -> None:
        super().age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


class Seed(Flower):

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        color: str,
        growth: float = 1.0
    ) -> None:
        super().__init__(name, height, age, color, growth)
        self._seeds: int = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.show_stats()


def main() -> None:
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.older_than_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.older_than_year(400)}")

    print("\n=== Flower")
    rose: Flower = Flower("Rose", 15.0, 10, "red", growth=8.0)
    rose.show()
    display_statistics(rose)
    print(f"[asking the {rose.name} to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_statistics(rose)

    print("\n=== Tree")
    oak: Tree = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_statistics(oak)
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    display_statistics(oak)

    print("\n=== Seed")
    sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow", 1.5)
    sunflower.show()
    print(f"[make the {sunflower.name} grow, age and bloom]")
    sunflower.grow(20)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    display_statistics(sunflower)

    print("\n=== Anonymous")
    unknown: Plant = Plant.anonymous()
    unknown.show()
    display_statistics(unknown)


if __name__ == "__main__":
    main()
