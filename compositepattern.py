class Iterator:
    def __init__(self):
        self.__items = []
        self.__pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__pos < len(self.__items):
            self.__pos += 1
            return self.__items[self.__pos - 1]
        else:
            self.__pos = 0
            raise StopIteration()

    def __getitem__(self, index):
        if index <  len(self.__items):
            return self.__items[index]
        else:
            raise IndexError("Index out of range")

    def add(self, item):
        self.__items.append(item)

    def delte(self, item):
        self.__items.remove(item)


class MenuComponent:
    def add(self):
        raise ValueError("Unsupported Operation")

    def remove(self):
        raise ValueError("Unsupported Operation")

    def getChildren(self, index):
        raise ValueError("Unsupported Operation")

    def getName(self):
        raise ValueError("Unsupported Operation")

    def getDescription(self):
        raise ValueError("Unsupported Operation")

    def getPrice(self):
        raise ValueError("Unsupported Operation")

    def isVegetarian(self):
        raise ValueError("Unsupported Operation")

    def printCommand(self):
        raise ValueError("Unsupported Operation")


class MenuItem(MenuComponent):
    def __init__(self, name, description, vegetarian, price):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def isVegetarian(self):
        return self.__vegetarian

    def printCommand(self):
        print("   " + self.getName(), end=" ")
        if self.isVegetarian():
            print("(v)", end="")
        print("  " + str(self.getPrice()))
        print("    -- " + self.getDescription())
        

class Menu(MenuComponent):
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__items = Iterator()

    def add(self, new_item):
        self.__items.add(new_item)

    def remove(self, item):
        self.__items.delte(item) 

    def getChiild(self, position):
        return self.__items[position]

    def getName(self):
        return self.__name

    def getDescription(self):
        return self.__description

    def printCommand(self):
        print("\n"+self.getName(), end="")
        print(",  "+self.getDescription())
        print("---------------------")
        for item in self.__items:
            item.printCommand()


class Waitress:
    def __init__(self, menu):
        self.__menu = menu

    def printMenu(self):
        self.__menu.printCommand()


pancakeHousemenu = Menu("PANCAKE HOUSE MENU", "Breakfast")
dinerMenu = Menu("DINER MENU", "Lunch")
cafeMenu = Menu("CAFE MENU", "Dinner")
dessertMenu = Menu("DESSERT MENU", "Dessert of course")

allMenus = Menu("All MENUS", "ALL menus combined")
allMenus.add(pancakeHousemenu)
allMenus.add(dinerMenu)
allMenus.add(cafeMenu)

dinerMenu.add(MenuItem("Pasta", "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 2.99))
dinerMenu.add(dessertMenu)

dessertMenu.add(MenuItem("Apple Pie", "Apple Pie with a flakey crust, topped with vanilla icecream", True, 1.59))

waitress = Waitress(allMenus)
waitress.printMenu()