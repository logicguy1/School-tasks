class Car:
    def __init__(self, brand, model, year, fule):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuleAmount = fule

    def fill_tank(self):
        self.fuleAmount += int(input("How much to fill up the car with?\n>>> "))


class ECar(Car):
    def __init__(self, brand, model, year, fule):
        super(ECar, self).__init__(brand, model, year, fule)

        self.battery = 70

    def show_battery(self):
        print(f"The battery is {self.battery} % full")

    def fill_tank(self):
        print("This is an EV, you cant put fule in it!!")


my_car = Car("BMW", "MP4WW", 2008, 0)

my_car.fill_tank()
print(my_car.fuleAmount)

my_ev = ECar("Tesla", "Y2", 2056, 30)
my_ev.show_battery()
my_ev.fill_tank()
