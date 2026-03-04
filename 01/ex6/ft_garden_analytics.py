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

    def __init__(self, name: str, height: int) -> None:
        """x"""
        self.name: str = name
        self.height: int = height
        self.category: str = "regular"
        self.score: int = height

    def grow(self, cm: int) -> None:
        """Increase height by cm."""
        self.height += cm
        print(f"{self.name} grew {cm}cm")

    def get_info(self) -> str:
        """Return formatted plant information."""
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """First level of inheritance."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """x"""
        super().__init__(name, height)
        self.color: str = color
        self.category: str = "flowering"

    def get_info(self) -> str:
        """x"""
        return super().get_info() + f" {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Second level of inheritance."""

    def __init__(
        self, name: str, height: int, color: str, points: int,
    ) -> None:
        """x"""
        super().__init__(name, height, color)
        self.points: int = points
        self.category: str = "prize flowers"
        self.score: int = height + points * 4

    def get_info(self) -> str:
        """x"""
        return super().get_info() + f" Prize points: {self.points}"


class GardenManager:
    """x"""

    total_gardens = 0

    class GardenStats:
        """z"""

        def __init__():
            """x"""
            pass

    def __init__(self, name: str):
        """x"""
        self.name: str = name

    @classmethod
    def create_garden_network(cls, sus muertos):
        """x"""
        jardin: garden = jardin
        GardenManager.total_gardens += 1
        print(f"Total gardens: {GardenManager.total_gardens}")

    @staticmethod
    def print_header() -> None:
        """x"""
        print("=== Garden Management System Demo ===")


def main() -> None:
    """x"""
    GardenManager.print_header()


if __name__ == "__main__":
    main()


"""
Build a comprehensive garden data analytics platform that processes and analyzes gar-
den data. This system needs to handle complex data relationships and provide detailed
analytics using nested components and inheritance chains.
Requirements:
• Create a GardenManager that can handle multiple gardens
• Include a helper GardenStats inside your manager for calculating statistics
• Include a method create_garden_network() that works on the manager type itself
• Add utility functions that don’t need specific garden data
• Show different types of methods: instance methods, class-level methods, and utility
functions
• Each garden should track plant collections and statistics
• Use your nested statistics helper to calculate analytics
• Organize everything within appropriate structures - avoid scattered global functions

Example:
Added Oak Tree to Alice's garden
Added Rose to Alice's garden
Added Sunflower to Alice's garden

Alice is helping all plants grow...
Oak Tree grew 1cm
Rose grew 1cm
Sunflower grew 1cm

=== Alice's Garden Report ===
Plants in garden:
- Oak Tree: 101cm
- Rose: 26cm, red flowers (blooming)
- Sunflower: 51cm, yellow flowers (blooming), Prize points: 10

Plants added: 3, Total growth: 3cm
Plant types: 1 regular, 1 flowering, 1 prize flowers
Height validation test: True
Garden scores - Alice: 218, Bob: 92
Total gardens managed: 2
"""

"""
[class Plant:

    def __init__(self, name: str, height: int) -> None:
        self.name: str = name
        self.height: int = height
        self.category: str = "regular"

    def grow(self, cm: int) -> None:
        self.height += cm
        print(f"{self.name} grew {cm}cm")

    def get_info(self) -> str:
        return f"- {self.name}: {self.height}cm"


class FloweringPlant(Plant):

    def __init__(self, name: str, height: int, color: str) -> None:
        super().__init__(name, height)
        self.color: str = color
        self.category: str = "flowering"

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):

    def __init__(
        self, name: str, height: int, color: str, points: int
    ) -> None:
        super().__init__(name, height, color)
        self.points: int = points
        self.category: str = "prize flowers"

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), Prize points: {self.points}"
        )


class GardenManager:

    total_gardens: int = 0

    class GardenStats:

        @staticmethod
        def calculate_score(plants: tuple) -> int:
            score: int = 0
            for p in plants:
                score += p.height
                if p.category == "prize flowers":
                    score += p.points * 4
            return score

        @staticmethod
        def get_counts(plants: tuple) -> tuple:
            reg: int = 0
            flow: int = 0
            prize: int = 0
            for p in plants:
                if p.category == "regular":
                    reg += 1
                elif p.category == "flowering":
                    flow += 1
                elif p.category == "prize flowers":
                    prize += 1
            return reg, flow, prize

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: tuple = ()
        self.total_growth: int = 0
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.plants += (plant,)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, cm: int) -> None:
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @classmethod
    def create_garden_network(cls, owner1: str, owner2: str) -> tuple:
        return (cls(owner1), cls(owner2))

    def generate_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        count: int = 0
        for p in self.plants:
            print(p.get_info())
            count += 1

        print(
            f"Plants added: {count}, Total growth: {self.total_growth}cm"
        )

        reg, flow, prize = self.GardenStats.get_counts(self.plants)
        print(
            f"Plant types: {reg} regular, {flow} flowering, "
            f"{prize} prize flowers"
        )

        is_valid: bool = True
        for p in self.plants:
            if not self.validate_height(p.height):
                is_valid = False
        print(f"Height validation test: {is_valid}")


def main() -> None:
    print("=== Garden Management System Demo ===")

    alice, bob = GardenManager.create_garden_network("Alice", "Bob")

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    bob_plant: Plant = Plant("Shrub", 92)
    bob.plants += (bob_plant,)

    alice.grow_all(1)
    alice.generate_report()

    score_a: int = GardenManager.GardenStats.calculate_score(alice.plants)
    score_b: int = GardenManager.GardenStats.calculate_score(bob.plants)
    print(f"\nGarden scores - Alice: {score_a}, Bob: {score_b}")

    print(f"\nTotal gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
]
"""