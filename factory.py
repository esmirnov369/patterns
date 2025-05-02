from enum import Enum
from abc import ABC, abstractmethod

# Abstract Factory
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self) -> Dough: pass
    @abstractmethod
    def create_sauce(self) -> Sauce: pass

# Concrete Factories
class NewYorkIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()
    def create_sauce(self) -> Sauce:
        return TomatoSauce()

class ChicagoIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()
    def create_sauce(self) -> Sauce:
        return SpicySauce()

# Products
class Dough(ABC): pass
class ThinCrustDough(Dough): pass
class ThickCrustDough(Dough): pass

class Sauce(ABC): pass
class TomatoSauce(Sauce): pass
class SpicySauce(Sauce): pass


class PizzaType(Enum):
    PEPPERONI = "pepperoni"
    MARGHERITA = "margherita"
    VEGGIE = "veggie"

class Pizza:
    def __init__(self, pizzatype):
        self.pizzatype = pizzatype
    
    def __str__(self):
        return f'Hi, I am a {self.pizzatype} pizza!'

class PizzaFactory:
    VALID_TYPES = {t.value for t in PizzaType}

    @staticmethod
    def create_pizza(pizzatype):
        if pizzatype not in PizzaFactory.VALID_TYPES:
            raise ValueError(f"Invalid pizza type: {pizzatype}")
        return Pizza(pizzatype)

if __name__ == "__main__":
    pep1 = PizzaFactory.create_pizza(PizzaType.PEPPERONI.value)
    print(pep1)  # Hi, I am a pepperoni pizza!

    from abc import ABC, abstractmethod

    # Usage
    ny_factory = NewYorkIngredientFactory()
    dough = ny_factory.create_dough()  # ThinCrustDough
    sauce = ny_factory.create_sauce()  # TomatoSauce   