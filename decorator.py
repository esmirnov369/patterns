from abc import ABC, abstractmethod

class Beverage(ABC):
    def __init__(self):
        self.description = "Unknown Beverage"

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


class DarkRoast(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Dark Roast Coffee"

    def cost(self):
        return 2.99  # Base price

class HouseBlend(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "House Blend Coffee"

    def cost(self):
        return 1.99  # Base price

class Espresso(Beverage):
    def __init__(self):
        super().__init__()
        self.description = "Espresso"

    def cost(self):
        return 1.99
    
class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage):
        self.beverage = beverage  # The beverage being decorated

@abstractmethod
def get_description(self):
    pass


class Mocha(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Mocha"

    def cost(self):
        return self.beverage.cost() + 0.50  # Mocha costs extra

class Whip(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Whip"

    def cost(self):
        return self.beverage.cost() + 0.70  # Whip costs extra

class Soy(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + ", Soy"

    def cost(self):
        return self.beverage.cost() + 0.30
    
class XmasCup(CondimentDecorator):
    def get_description(self):
        return self.beverage.get_description() + " in a holiday themed cup!"

    def cost(self):
        return self.beverage.cost() * 2



    # Order a Dark Roast with Mocha and Whip
dark_roast = DarkRoast()
dark_roast = Mocha(dark_roast)  # Add Mocha
dark_roast = XmasCup(Whip(dark_roast))   # Add Whip and a cup

print(f"{dark_roast.get_description()} = ${dark_roast.cost():.2f}")
# Output: "Dark Roast Coffee, Mocha, Whip = $4.19"

# Order a House Blend with Soy and Mocha
house_blend = HouseBlend()
house_blend = Soy(house_blend)  # Add Soy
house_blend = Mocha(house_blend)  # Add Mocha

print(f"{house_blend.get_description()} = ${house_blend.cost():.2f}")
# Output: "House Blend Coffee, Soy, Mocha = $2.79"