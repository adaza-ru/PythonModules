#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_garden_analytics.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: adaza-ru <adaza-ru@student.42malaga.com>     +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/04 01:43:03 by adaza-ru            #+#    #+#            #
#   Updated: 2026/03/04 01:54:06 by adaza-ru           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    """Base class in the plant family tree."""

    def __init__(self, name: str, height: int, garden: 'Garden') -> None:
        """x"""
        self.name: str = name
        self.height: int = height
        self.category: str = "regular"
        garden.add_plant_to_garden(self)

    def grow(self, cm: int) -> None:
        """Increase height by cm."""
        self.height += cm
        print(f"{self.name} grew {cm}cm")

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """First level of inheritance."""

    def __init__(
        self, name: str, height: int, garden: 'Garden', color: str
    ) -> None:
        """x"""
        super().__init__(name, height, garden)
        self.color: str = color
        self.category: str = "flowering"

    def get_info(self) -> str:
        """x"""
        return super().get_info() + f" {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Second level of inheritance."""

    def __init__(
        self, name: str, height: int, garden: 'Garden', color: str, points: int,
    ) -> None:
        """x"""
        super().__init__(name, height, garden, color)
        self.points: int = points
        self.category: str = "prize flowers"

    def get_info(self) -> str:
        """x"""
        return super().get_info() + f" Prize points: {self.points}"

             
class Garden:
    """x"""

    total_gardens: int = 0

    def __init__(self, name: str, manager: 'GardenManager') -> None:
        """x"""
        self.plants: list[Plant] = []
        self.name: str = name
        self.owner: str = manager.name
        self.number_of_plants = 0
        Garden.count_garden()
        manager.add_garden_to_manager(self)
    
    @classmethod
    def count_garden(cls) -> None:
        """x"""
        cls.total_gardens += 1

    def add_plant_to_garden(self, plant: Plant) -> None:
        """x"""
        self.plants += [plant]
        self.number_of_plants += 1
        print(f"{plant.name} grew in {self.name}'s garden")


class GardenManager:
    """x"""

    total_managers: int = 0
    managers: list['GardenManager'] = []

    class GardenStats:
        """x"""

        def calculate_score(gardens: list):
            """x"""

    def __init__(self, name: str) -> None:
        """x"""
        self.name: str = name
        self.gardens: list[Garden] = []
        self.number_of_gardens: int = 0
        self.work_done: int = 0
        self.welcome()
        GardenManager.managers += [self]
        GardenManager.create_garden_network()

    def welcome(self):
        """x"""
        print(f"Let's welcome our new Manager: {self.name}. ", end="")

    @classmethod
    def create_garden_network(cls) -> None:
        """x"""
        cls.total_managers += 1
        print(f"Number of managers: {cls.total_managers}")

    def add_garden_to_manager(self, garden: Garden) -> None:
        """x"""
        self.gardens += [garden]
        self.number_of_gardens += 1
        print(f"{self.name} is managing {garden.name}'s garden")

    def grow_plants(self):
        """x"""
        print(f"{self.name} is helping all plants grow...")
        for g in self.gardens:
            for p in g.plants:
                p.grow(1)
                self.work_done += 1

    @staticmethod
    def print_header() -> None:
        """x"""
        print("=== Garden Management System Demo ===")

    def create_report(self) -> None:
        """x"""
        regular_plants: int = 0
        flowering_plants: int = 0
        prize_flowers: int = 0
        height_bool: bool = True
        print(f"=== {self.name}'s Garden Report ===")
        for g in self.gardens:
            print(f"Plants in {g.name}'s garden:")
            for p in g.plants:
                if p.height < 0:
                    height_bool = False
                print(f"{p.get_info()}")
                if p.category == "regular":
                    regular_plants += 1
                elif p.category == "flowering":
                    flowering_plants += 1
                elif p.category == "prize flowers":
                    prize_flowers += 1
        total_plants: int = regular_plants + flowering_plants + prize_flowers
        print(f"Plants added: {total_plants}", end="")
        print(f", Total growth: {self.work_done}cm")
        print(f"Plant types: {regular_plants} regular, ", end="")
        print(f"{flowering_plants} flowering, ", end="")
        print(f"{prize_flowers} prize flowers\n")
        print(f"Height validation test: {height_bool}")


def main() -> None:
    """x"""
    GardenManager.print_header()
    bob: GardenManager = GardenManager("Bob")
    alice: GardenManager = GardenManager("Alice")
    print("")
    garden_bob: Garden = Garden("Parque De Los Patos", bob)
    garden_alice: Garden = Garden("Parque Maria Zambrano", alice)
    print("")
    Plant("Bamboo", 200, garden_bob)
    print("")
    FloweringPlant("Poppy", 30, garden_alice, "red")
    Plant("Peyote", 30, garden_alice)
    PrizeFlower("Maria", 150, garden_alice, "green", 100)
    print("")
    alice.grow_plants()
    print("")
    alice.create_report()
    print("Garden scores - ")
    print(f"Alice: {alice.GardenStats.calculate_score}", end="")
    print(f", Bob: {bob.GardenStats.calculate_score}")
    print(f"Total gardens managed: {Garden.total_gardens}")


if __name__ == "__main__":
    main()

"""
• Include a helper GardenStats inside your manager for calculating statistics

Garden scores - Alice: 218, Bob: 92
Total gardens managed: 2

"""
