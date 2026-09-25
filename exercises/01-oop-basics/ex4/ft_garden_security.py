#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:45:28 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/14 18:23:26 by adaza-ru           ###   ########.fr      #
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

    def grow(self, times: int | None = None) -> None:

        self._height += (
            self._growth_rate if times is None else self._growth_rate * times
        )

    def age(self, days: int = 1) -> None:

        self._days += days

    def show(self) -> None:
        print(self)


def main() -> None:

    print("=== Garden Security System ===")
    rose: Plant = Plant("Rose", 15, 10)
    print("Plant created: ", end="")
    rose.show()
    print("")

    rose.set_height(25)
    rose.set_age(30)
    print("")

    rose.set_height(-25)
    rose.set_age(-30)
    print("")

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
