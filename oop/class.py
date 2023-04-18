class Vehicle:
    # class variable
    jumlah = 0

    def __init__(self, inputName, inputMerk, inputYear, inputCondition):
        self.name = inputName
        self.merk = inputMerk
        self.year = inputYear
        self.condition = inputCondition
        Vehicle.jumlah += 1

    def run(self):
        print(self.name, "run bitch ruuuuunnnn bbbrrrmmmmmm")

    def tabrak(self, speed):
        print("tabrak with ", speed, "km/h")
        self.condition = "broken"

    def getCondition(self):
        return self.condition


vehicle1 = Vehicle("agya", "toyota", 2000, "good")
vehicle2 = Vehicle("evo", "toyota", 2010, "good")

print(vehicle1.__dict__)
print(vehicle2.__dict__)
print(Vehicle.jumlah)
vehicle1.run()
vehicle1.tabrak(100)
print(vehicle1.getCondition())
