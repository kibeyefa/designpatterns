from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    def __init__(self, **kwargs):
        self.condiments = kwargs["condiments"]

    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.condiments:
            self.addCondiment()

    def boilWater(self):
        print("Boiling water...")
    
    def pourInCup(self):
        print("Pouring in cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiment(self):
        pass


class Tea(CaffeineBeverage):
    """
    Creates a new Tea beverage
    Specify condiments=True to add condiments
    """
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
    
    def brew(self):
        print("Steeping Tea in water")

    def addCondiment(self):
        print("Adding lemon to tea")


class Coffee(CaffeineBeverage):
    """
    Creates a new Coffee beverage
    Specify condiments=True to add condiments
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def brew(self):
        print("Brewing coffee grinds")

    def addCondiment(self):
        print("Adding sugar and milk.")

myTea = Tea(condiments=True)
myTea.prepareRecipe()
myCoffe = Coffee(condiments=True)
myCoffe.prepareRecipe()
