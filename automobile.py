class Automobile(object):
    def __init__(self, make, model, milage, price):
        self.__make = make 
        self.__model = model
        self.__milage = milage
        self.__price = price

    def set_make(self, make):
        self.__make = make 

    def set_model(self, model):
        self.__model = model 

    def set_milage(self, milage):
        self.__milage = milage

    def set_price(self, price):
        self.__price = price

    def get_make(self, make):
        return self.__make  

    def get_model(self, model):
        return self.__model 

    def get_milage(self, milage):
        return self.__milage

    def get_price(self, price):
        return self.__price

class car(Automobile):
    def __init__(self, make, model, milage, price, doors):
        Automobile.__init__(make, model, milage, price)

        self.__doors = doors 

    def set_doors(self, doors):
        self.__doors = doors

    def get_doors(self, doors):
        return self.__doors

daves_car = Automobile("Toyota", "Corolla", 3600, 23000)

class Truck(Automobile):
    def __init__(self, make, model, milage, price, drivetrain):
        Automobile.__init(self, make, model, milage, price)

        self.__drivetrain = drivetrain

    def set_drivetrain(self, drivetrain):
        self.__drivetrain = drivetrain

    def get_drivetrain(self, drivetrain):
        return self.__drivetrain

    def __str__(self):
        return f"""
