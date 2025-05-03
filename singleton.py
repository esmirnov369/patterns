class Singleton:
    _instance = None  # This will hold the single instance

    def __new__(cls):
        if cls._instance is None:  # If no instance exists yet
            cls._instance = super().__new__(cls)  # Create one
        return cls._instance  # Always return the same instance

# Testing
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # Output: True (they are the same object)