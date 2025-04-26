# Step 1: Define the Subject
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = 0

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()


# Step 2: Define the Observer Interface
class Observer:
    def update(self, temperature):
        pass


# Step 3: Create Concrete Observers
class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f"Phone display updated: Temperature is now {temperature}°C")


class WeatherApp(Observer):
    def update(self, temperature):
        print(f"Weather app updated: Temperature is now {temperature}°C")


# Step 4: Putting It All Together
if __name__ == "__main__":
    # Create a WeatherStation
    weather_station = WeatherStation()

    # Create observers
    phone_display = PhoneDisplay()
    weather_app = WeatherApp()

    # Register observers
    weather_station.register_observer(phone_display)
    weather_station.register_observer(weather_app)

    # Set the temperature and notify observers
    weather_station.set_temperature(25)  # Both observers will be notified
    weather_station.set_temperature(30)  # Both observers will be notified
