#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_data.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/08 15:53:18 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/14 18:23:01 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


class Plant:

    def __init__(self, name: str, height: int, age: int) -> None:

        self.name: str = name
        self.height: int = height
        self.days: int = age

    def __str__(self) -> str:

        return f"{self.name}: {self.height}cm, {self.days} days old"

    def show(self) -> None:

        print(self)


def display_garden(plants: list[Plant]) -> None:

    print("=== Garden Plant Registry ===")
    for plant in plants:
        plant.show()


def main() -> None:

    raw_data: list[Plant] = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120),
    ]

    display_garden(raw_data)


if __name__ == "__main__":
    main()
