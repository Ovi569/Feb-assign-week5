# Class representing types of Food
class Food:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price

    def eat(self):
        print(f"Eating {self.name}...")

    def describe(self):
        print(f"{self.name} is a {self.category} food priced at ${self.price}.")

# Subclass representing Vegetables (inheritance)
class Vegetable(Food):
    def __init__(self, name, category, price, freshness):
        super().__init__(name, category, price)
        self.freshness = freshness

    def cook(self):
        print(f"Cooking {self.name}, which is {self.freshness} fresh.")

# Polymorphism Challenge: Foods with different prepare() methods
class FoodItem:
    def prepare(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Fruit(FoodItem):
    def prepare(self):
        print("Washing and slicing the fruit 🍎")

class Meat(FoodItem):
    def prepare(self):
        print("Marinating and grilling the meat 🍖")

class Dessert(FoodItem):    
    def prepare(self):
        print("Baking and decorating the dessert 🍰"
              )

# Polymorphism Challenge: Vehicles with different move() methods
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example usage
if __name__ == "__main__":
    # Smartphone and Smartwatch
    phone = Smartphone("Apple", "iPhone 14", 999)
    phone.call("123-456-7890")
    phone.browse("www.example.com")

    watch = Smartwatch("Samsung", "Galaxy Watch 5", 299, "24 hours")
    watch.track_steps(5000)

    # Polymorphism with vehicles
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()