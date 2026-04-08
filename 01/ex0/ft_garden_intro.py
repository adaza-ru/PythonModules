#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_garden_intro.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/08 15:53:30 by adaza-ru            #+#    #+#            #
#   Updated: 2026/04/08 16:07:55 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_garden_intro(plant: str, cm: int, days: int) -> None:
    name: str = plant
    height: int = cm
    age: int = days

    print("=== Welcome to My Garden ===")
    print(f"Plant: {name}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, 30)
