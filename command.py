from abc import ABC, abstractmethod

# ----- 1. Receiver (Performs the actual work) -----
class Chef:
    def prepare_pizza(self):
        print("Chef: Cooking a delicious pizza!")

    def prepare_pasta(self):
        print("Chef: Cooking creamy pasta!")

    def cancel_pizza(self):
        print("Chef: Throwing away the pizza dough.")

    def cancel_pasta(self):
        print("Chef: Putting pasta back in storage.")

# ----- 2. Command Interface -----
class OrderCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# ----- 3. Concrete Commands (Encapsulate actions) -----
class PizzaOrder(OrderCommand):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        self.chef.prepare_pizza()

    def undo(self):
        self.chef.cancel_pizza()

class PastaOrder(OrderCommand):
    def __init__(self, chef):
        self.chef = chef

    def execute(self):
        self.chef.prepare_pasta()

    def undo(self):
        self.chef.cancel_pasta()

# ----- 4. Invoker (Triggers commands) -----
class Waiter:
    def __init__(self):
        self._orders = []
        self._current_order = None

    def take_order(self, order):
        self._current_order = order
        self._orders.append(order)
        print("Waiter: Order received!")

    def submit_order(self):
        if self._current_order:
            self._current_order.execute()
        else:
            print("Waiter: No order to submit.")

    def cancel_last_order(self):
        if self._orders:
            order = self._orders.pop()
            order.undo()
            print("Waiter: Last order canceled.")
        else:
            print("Waiter: No orders to cancel.")

# ----- 5. Client (Customer placing orders) -----
if __name__ == "__main__":
    # Setup
    chef = Chef()
    waiter = Waiter()

    # Customer orders
    pizza_order = PizzaOrder(chef)
    pasta_order = PastaOrder(chef)

    # Waiter takes orders
    waiter.take_order(pizza_order)
    waiter.take_order(pasta_order)

    # Submit orders to kitchen
    print("\n--- Preparing orders ---")
    waiter.submit_order()  # Pizza is cooked
    waiter.submit_order()  # Pasta is cooked

    # Undo last order (Cancel pasta)
    print("\n--- Canceling last order ---")
    waiter.cancel_last_order()  # Pasta is canceled