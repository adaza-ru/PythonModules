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
        self.name: str = name
        self.height: int = height
        self.category: str = "regular"

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
        super().__init__(name, height)
        self.color: str = color
        self.category: str = "flowering"

    def get_info(self) -> str:
        return (
            f"- {self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    """Second level of inheritance."""

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
    """Handles multiple gardens and overall analytics."""

    total_gardens: int = 0

    class GardenStats:
        """Nested helper class exclusively for calculating statistics."""

        @staticmethod
        def calculate_score(plants: tuple) -> int:
            """Calculate arbitrary score based on height and points."""
            score: int = 0
            for p in plants:
                score += p.height
                if p.category == "prize flowers":
                    score += p.points * 4
            return score

        @staticmethod
        def get_counts(plants: tuple) -> tuple:
            """Tally the different types of plants."""
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
        """Add a plant to the garden's collection."""
        self.plants += (plant,)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self, cm: int) -> None:
        """Help all plants in this specific garden grow."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(cm)
            self.total_growth += cm

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility function: doesn't need 'self' or 'cls'."""
        return height >= 0

    @classmethod
    def create_garden_network(cls, owner1: str, owner2: str) -> tuple:
        """Class method acting as a factory for multiple gardens."""
        return (cls(owner1), cls(owner2))

    def generate_report(self) -> None:
        """Generate full analytics report for this garden."""
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
