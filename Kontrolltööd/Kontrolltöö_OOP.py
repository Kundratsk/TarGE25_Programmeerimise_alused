import random

class House:
    """
    Represents a general house with basic features.

    Attributes:
        house_count (int): Class variable to track the total number of houses created.
    """
    house_count = 0

    def __init__(self, address, rooms, floors):
        """
        Initializes a new house instance.

        Args:
            address (str): The physical address of the house.
            rooms (int): Number of rooms in the house.
            floors (int): Number of floors in the house.
        """
        self.address = address
        self.rooms = rooms
        self.floors = floors
        House.house_count += 1

    def display_info(self):
        """Prints out the basic information of the house."""
        return f"House at {self.address} has {self.rooms} rooms, {self.floors} floors."

    def renovate(self, new_room_count):
        """
        Changes the number of rooms during renovation.

        Args:
            new_room_count (int): The updated number of rooms.
        """
        if new_room_count > 0:
            self.rooms = new_room_count
            print(f"Renovation complete! New room count: {self.rooms}")
        else:
            print(f"Error: Room count '{new_room_count}' is invalid. can not be negative!")

    def estimate_value(self):
        """
        Calculates an estimated price for the house.

        Returns:
            int: The estimated value in Euros.
        """
        return (self.rooms * 15000) + (self.floors * 20000)


class PrivateHouse(House):
    """
    Represents a private house, inheriting from House.
    Demonstrates polymorphism by overriding the value estimation.
    """

    def __init__(self, address, rooms, floors, garden_size=500):
        """
        Initializes a private house with an additional garden size field.

        Args:
            address (str): The physical address.
            rooms (int): Number of rooms.
            floors (int): Number of floors.
            garden_size (int, optional): Size of the garden in sqm. Defaults to 500.
        """
        super().__init__(address, rooms, floors)
        self.garden_size = garden_size

    def maintain_garden(self):
        """Simulates garden maintenance work."""
        return f"The {self.garden_size} square meter garden at {self.address} has been maintained."

    def estimate_value(self):
        """
        Calculates an estimated price including the garden value (Polymorphism).

        Returns:
            int: The total estimated value.
        """
        base_value = super().estimate_value()
        garden_value = self.garden_size * 50
        return base_value + garden_value



if __name__ == '__main__':

    test_house = House("Sõpruse pst 10", 3, 1)
    print(test_house.display_info())
    print(f"Initial value: {test_house.estimate_value()} €")

    test_house.renovate(-5)
    test_house.renovate(5)

    house_list = []

    for i in range(60):
        house_list.append(House(f"Ehitajate tee {i+1}", random.randint(1, 4), 1))

    for i in range(40):
        house_list.append(PrivateHouse(f"Mereranna tee {i+1}", random.randint(3, 6), 2, 750))

    print("\n--- Value Estimation (Every 20th house) ---")
    for index, house in enumerate(house_list):
        if index % 20 == 0:
            val = house.estimate_value()
            print(f" {index}: {house.address} is worth approximately {val} €")

    print(f"\nTotal houses created: {House.house_count}")
