class CheesePizza:
    def __init__(self) -> None:
        self.type = "cheese"

    def __str__(self) -> str:
        return "Cheese Pizza"

class PepperoniPizza:
    def __init__(self) -> None:
        self.type = "pepperoni"

    def __str__(self) -> str:
        return "Pepperoni Pizza"

class ClamPizza:
    def __init__(self) -> None:
        self.type = "clam"

    def __str__(self) -> str:
        return "Clam Pizza"

class SimplePizzaFactory:
    def __init__(self, type) -> None:
        self._type = type.lower()
        # self.pizza = None

    def createPizza(self):
        if self._type == "cheese":
            self.pizza = CheesePizza()

        elif self._type == "clam":
            self.pizza = ClamPizza()
        return self.pizza

class PizzaStore:
    def __init__(self, factory: SimplePizzaFactory):
        self._factory = factory
        
    def orderPizza(self, type: str):
        pizza = self._factory.createPizza(type.lower())
        return pizza