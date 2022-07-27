class Car:
    wheels = 4

    def __init__(self, model, color, owner, year):
        self.model = model
        self.mileage = 0
        self.tank = 0
        self.color = color
        self.owner = owner
        self.year = year

    def get_fuel(self, liters):
        self.tank += liters
        print(
            f"You just got {liters} liters and, in total, you got {self.tank} liters in your in tank")
        return self.tank

    def driving(self, km=int):
        liters = km * 0.1
        if self.tank >= liters:
            print(f"{self.owner}, worry not! Drive ahead, baby!")
            self.mileage += km
            self.tank -= liters
        else:
            print("You got no enough gas in your tank!!!")

    def change_color(self, new_color):
        self.color = new_color
        print(f"You changed the color of your {self.model}")


vehicle_one = Car("BMW", "black-stripped yellow", 'uLN', 2020)
vehicle_two = Car("Audi", "sky-blue", 'Kunduz', 2019)
vehicle_one.change_color("White")

# vehicle_one.get_fuel(9)
# vehicle_one.driving(100)

# print("*" * 10)
# print("*" * 10)

# vehicle_two.get_fuel(40)
# vehicle_two.driving(150)
