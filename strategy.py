from abc import ABC, abstractmethod

# Step 1: Create the Strategy Interface


class TravelStrategy(ABC):
    @abstractmethod
    def travel(self):
        pass

# Step 2: Create concrete strategy classes


class CarTravel(TravelStrategy):
    def travel(self):
        return "Traveling by car."


class BikeTravel(TravelStrategy):
    def travel(self):
        return "Traveling by bike."


class AirplaneTravel(TravelStrategy):
    def travel(self):
        return "Traveling by airplane."

# Step 3: Create the context class that uses the strategies


class Traveler:
    def __init__(self, strategy: TravelStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self.strategy = strategy

    def travel(self):
        return self.strategy.travel()


# Step 4: Using the strategy pattern
if __name__ == "__main__":
    traveler = Traveler(CarTravel())
    print(traveler.travel())  # Outputs: Traveling by car.

    traveler.set_strategy(AirplaneTravel())
    print(traveler.travel())  # Outputs: Traveling by airplane.

    traveler.set_strategy(BikeTravel())
    print(traveler.travel())  # Outputs: Traveling by bike.
