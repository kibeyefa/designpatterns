class ChocolateBoiler:

    __uniqueBoilers = None

    @staticmethod
    def get_uniqueBoiler():
        if ChocolateBoiler.__uniqueBoilers == None:
            ChocolateBoiler()
        return ChocolateBoiler.__uniqueBoilers

    def __init__(self):
        if ChocolateBoiler.__uniqueBoilers == None:
            ChocolateBoiler.__uniqueBoilers = self
            self.__empty = True
            self.__boiled = False
        else:
            raise Exception("ChocolateBoiler can't be instantiated more than once!")

    def is_empty(self):
        return self.__empty

    def is_boiled(self):
        return self.__boiled

    def fill(self):
        if self.__empty == True:
            self.__empty = False
            self.__boiled = False

    def boil(self):
        if self.__empty == True and self.__boiled == False:
            self.__boiled = True

    def drain(self):
        if self.__empty == False and self.__boiled == True:
            self.__empty = True

c = ChocolateBoiler().get_uniqueBoiler()
c.fill()
c.boil()
print(c.is_boiled())

c2 = ChocolateBoiler()
