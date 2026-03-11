class Plant:
    """Base class in the plant family tree."""

    def __init__(self, name: str, height: int, garden: 'Garden') -> None:
        """Initialize a basic plant and add it to a garden."""
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
    """First level of inheritance representing a flowering plant."""

    def __init__(
        self, name: str, height: int, garden: 'Garden', color: str
    ) -> None:
        """Initialize a flowering plant with a specific color."""
        super().__init__(name, height, garden)
        self.color: str = color
        self.category: str = "flowering"

    def get_info(self) -> str:
        """Return formatted info including blooming status and color."""
        return super().get_info() + f" {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Second level of inheritance representing a prize-winning flower."""

    def __init__(
        self, name: str, height: int, garden: 'Garden',
        color: str, points: int,
    ) -> None:
        """Initialize a prize flower with competition points."""
        super().__init__(name, height, garden, color)
        self.points: int = points
        self.category: str = "prize flowers"

    def get_info(self) -> str:
        """Return formatted info including prize points."""
        return super().get_info() + f" Prize points: {self.points}"


class Garden:
    """Represents a garden containing multiple plants."""

    total_gardens: int = 0

    def __init__(self, name: str, manager: 'GardenManager') -> None:
        """Initialize a garden and link it to its manager."""
        self.plants: list[Plant] = []
        self.name: str = name
        # RESTAURAMOS EL CONTADOR: Ya que no hay len(), lo necesitamos.
        self.number_of_plants: int = 0 
        Garden.count_garden()
        manager.add_garden_to_manager(self)

    def add_plant_to_garden(self, plant: Plant) -> None:
        """Add a newly created plant to this garden."""
        # ALTERNATIVA A APPEND: Sumamos una lista con otra
        self.plants += [plant] 
        # Aumentamos el contador manual
        self.number_of_plants += 1 
        print(f"{plant.name} grew in {self.name}'s garden")

    @classmethod
    def count_garden(cls) -> None:
        """Increment the global count of gardens."""
        cls.total_gardens += 1


class GardenManager:
    """Manages multiple gardens and their statistics."""

    total_managers: int = 0

    class GardenStats:
        """Handles statistical calculations for a manager's gardens."""

        @staticmethod
        def calculate_score(gardens: list['Garden']) -> int:
            """Calculate total score based on plant heights and prize points"""
            total_score: int = 0
            for g in gardens:
                for p in g.plants:
                    if isinstance(p, PrizeFlower):
                        total_score += p.height + (p.points * 4)
                    else:
                        total_score += p.height
            return total_score

    def __init__(self, name: str) -> None:
        """Initialize the manager with a name and empty garden list."""
        self.name: str = name
        self.gardens: list[Garden] = []
        self.number_of_gardens: int = 0
        self.work_done: int = 0
        self.welcome()
        GardenManager.create_garden_network()

    def welcome(self) -> None:
        """Print a welcome message for the new manager."""
        print(f"Let's welcome our new Manager: {self.name}. ", end="")

    @classmethod
    def create_garden_network(cls) -> None:
        """Increment the global manager count and display it."""
        cls.total_managers += 1
        print(f"Number of managers: {cls.total_managers}")

    def add_garden_to_manager(self, garden: Garden) -> None:
        """Add a garden to the manager's supervision."""
        # ALTERNATIVA A APPEND
        self.gardens += [garden] 
        self.number_of_gardens += 1
        print(f"{self.name} is managing {garden.name}'s garden")

    def grow_plants(self) -> None:
        """Increase the height of all plants in all managed gardens."""
        print(f"{self.name} is helping all plants grow...")
        for g in self.gardens:
            for p in g.plants:
                p.grow(1)
                self.work_done += 1

    @staticmethod
    def print_header() -> None:
        """Display the system's main header."""
        print("=== Garden Management System Demo ===")

    def create_report(self) -> None:
        """Generate a detailed report of all managed gardens and plants."""
        regular_plants: int = 0
        flowering_plants: int = 0
        prize_flowers: int = 0
        height_bool: bool = True
        
        print(f"=== {self.name}'s Garden Report ===")
        print(f"Managing {self.number_of_gardens} garden(s).")
        
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
        print(f"{prize_flowers} prize flowers")
        print(f"Height validation test: {height_bool}\n")


def main() -> None:
    """Run the main demonstration of the Garden Management System."""
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
    
    print("Garden scores - ", end="")
    # Aquí faltaban los paréntesis y pasarle las listas de jardines:
    alice_score: int = alice.GardenStats.calculate_score(alice.gardens)
    bob_score: int = bob.GardenStats.calculate_score(bob.gardens)
    
    print(f"Alice: {alice_score}", end="")
    print(f", Bob: {bob_score}")
    print(f"Total gardens managed: {Garden.total_gardens}")


if __name__ == "__main__":
    main()