from abc import ABC, abstractmethod

class Beverage(ABC):
    
    def __init__(self):
        self.description = "Unknown beverage"

    def getDescription(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass

class CondimentDecorator(Beverage):
    def getDescription(self):
        pass

class HouseBlend(Beverage):

    def __init__(self):
        self.description = "House Blend"

    def cost(self):
        return 0.89

class DarkRoast(Beverage):

    def __init__(self):
        self.description = "Dark Roast"

    def cost(self):
        return 0.99

class Espresso(Beverage):

    def __init__(self):
        self.description = "Espresso"

    def cost(self):
        return 1.99

class Decaf(Beverage):

    def __init__(self):
        self.description = "Decaf"

    def cost(self):
        return 1.05

class Mocha(CondimentDecorator):

    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Mocha"
    
    def cost(self):
        return 0.20 + self.beverage.cost()

class SteamedMilk(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Steamed Milk"

    def cost(self):
        return 0.10 + self.beverage.cost()
 

class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Soy"

    def cost(self):
        return 0.15 + self.beverage.cost()

class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self.beverage = beverage

    def getDescription(self):
        return self.beverage.getDescription() + ", Whip"

    def cost(self):
        return 0.10 + self.beverage.cost()
 
class StarBuzzCoffe:
    
    classmethod
    def CreateCoffee(cls, beverage):
        if beverage.capitalize() == "House Blend Coffe":
            new_beverage = HouseBlend()
        elif beverage.capitalize() == "Dark Roast":
            new_beverage = DarkRoast()
        elif beverage.capitalize() == "Decaf":
            new_beverage = Decaf()
        elif beverage.capitalize() == "Espresso":
            new_beverage = Espresso()

        return new_beverage

    classmethod
    def addCondiment(cls, beverage: Beverage, condiment):

        if condiment.capitalize() == "Whip":
            new_beverage = Whip(beverage)
        elif condiment.capitalize() == "Soy":
            new_beverage = Soy(beverage)
        elif condiment.capitalize() == "Steamed Milk":
            new_beverage = SteamedMilk(beverage)
        elif condiment.capitalize() == "Mocha":
            new_beverage = Mocha(beverage)

        return new_beverage

    classmethod
    def orderCoffee(cls, beverage: Beverage, condiments):

        for condiment in condiments:
            beverage = StarBuzzCoffe().addCondiment(beverage, condiment)
        
        return beverage

x = StarBuzzCoffe().orderCoffee(Espresso(), ["Whip", "Whip", "Soy"])
print(x.cost())



