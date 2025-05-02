from enum import Enum

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