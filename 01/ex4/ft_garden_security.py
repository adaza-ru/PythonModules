#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_security.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 00:45:28 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/04 01:18:20 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class SecurePlant:
    """
    A class that ensures data integrity for plant records.

    Attributes:
        __name (str): Private plant name.
        __height (int): Private height in cm (must be >= 0).
        __age (int): Private age in days (must be >= 0).
    """

    def __init__(self, name: str) -> None:
        """Initialize a SecurePlant with a name and default values."""
        self.__name: str = name
        self.__height: int = 0
        self.__age: int = 0
        print(f"Plant created: {self.__name}\n")

    def set_height(self, value: int) -> None:
        """Validate and set the plant height."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]\n")

    def set_age(self, value: int) -> None:
        """Validate and set the plant age."""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected\n")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]\n")

    def get_height(self) -> int:
        """Return the current protected height."""
        return self.__height

    def get_age(self) -> int:
        """Return the current protected age."""
        return self.__age

    def get_info(self) -> str:
        """Return formatted plant status."""
        return (
            f"Current plant: {self.__name} "
            f"({self.__height}cm, {self.__age} days)"
        )


def main() -> None:
    """Main simulation of the security system."""
    print("=== Garden Security System ===")
    rose: SecurePlant = SecurePlant("Rose")
    rose.set_height(25)
    rose.set_age(30)
    rose.set_height(-5)
    print(rose.get_info())


if __name__ == "__main__":
    main()
