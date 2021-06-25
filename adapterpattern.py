class Duck:

    def quack(self):
        pass

    def fly(self):
        pass

class Turkey:

    def gobble(self):
        pass

    def fly(self):
        print("I'm Flying!")

class MarladDuck(Duck):

    def quack(self):
        print("Quack")

    def fly(self):
        print("I'm Flying!")

class TurkeyAdapter(Duck):

    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()

