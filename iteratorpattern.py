class MenuItem:
    def __init__(self, name, description, vegetarian, price):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

    def getVegetarian(self):
        return self.vegetarian

    def __repr__(self):
        return "{} {} {} {}".format(self.name, self.description, self.vegetarian, self.price)


class Iterator:
    def __init__(self):
        self.item = []
        self.position = 0

    def __next__(self):
        if self.position < len(self.item):
            self.position += 1
            return self.item[self.position - 1]
        else:
            self.position = 0
            raise StopIteration()

    def __len__(self):
        return len(self.item)

    def __getitem__(self, i):
        if i < len(self):
            return self.item[i]
        else:
            return "Menu index out of range"

    def __setitem__(self, i, val):
        if i not in self.item:
            self.item[i] = val

    def __iter__(self):
        return self

    def index(self, i):
        return self.item.index(i)

    def remove(self):
        del self.item[-1]


class LunchMenu(Iterator):
    def __init__(self):
        super().__init__()
        self.maxitem = 6
        self.no_of_item = len(self.item)
        self.addItem(
            "Vegetarian BLT", "(Fakin’) Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.addItem(
            "BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.addItem(
            "Soup of the day", "Soup of the day, with a side of potato salad", False, 3.29)
        self.addItem(
            "Hotdog", "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05)

    def addItem(self, name, description, vegetarian, price):
        new_item = MenuItem(name, description, vegetarian, price)
        if len(self.item) <= self.maxitem:
            self.item.append(new_item)


class PancakeHouseMenu(Iterator):
    def __init__(self):
        super().__init__()
        self.addItem("K & B’s Pancake Breakfast",
                     "Pancakes with scrambled eggs, and toast", True, 2.99)
        self.addItem("Regular Pancake Breakfast",
                     "Pancakes with fried eggs, sausage", False, 2.99)
        self.addItem("Blueberry Pancakes",
                     "Pancakes made with fresh blueberries", True, 3.49)
        self.addItem("Waffles",
                     "Waffles, with your choice of blueberries or strawberries", True, 3.59)

    def addItem(self, name, description, vegetarian, price):
        new_item = MenuItem(name, description, vegetarian, price)
        self.item.append(new_item)


class CafeMenu(Iterator):
    def __init__(self):
        super().__init__()
        self.menuitems = {}
        self.addItem("Veggie Burger and Air Fries", "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99);
        self.addItem("Soup of the day", "A cup of the soup of the day, with a side salad", False, 3.69);
        self.addItem("Burrito", "A large burri with whole pinto beans, salsa, guacamole", True, 4.29)

    def addItem(self, name, description, vegetarian, price):
        new_item = MenuItem(name, description,vegetarian, price)
        self.menuitems[new_item.name] = new_item
        self.item.append(new_item)


class Waitress:
    def __init__(self, pancake_house_menu, lunch_house_menu, dinner_house_menu):
        self.pancake_house_menu = pancake_house_menu
        self.dinner_house_menu = dinner_house_menu
        self.lunch_house_menu = lunch_house_menu

    def printMenu(self):
        print("MENU\n----")
        self.printBreakfastMenu()
        self.printLunchMenu()
        self.printDinnerMenu()
        

    def printBreakfastMenu(self):
        print("\nBREAKFAST")
        print(self.__printMenu(self.pancake_house_menu))

    def printDinnerMenu(self):
        print("\nDINNER")
        print(self.__printMenu(self.dinner_house_menu))

    def printLunchMenu(self):
        print("\nLUNCH")
        print(self.__printMenu(self.lunch_house_menu))

    def __printMenu(self, iterators):
        for i in iterators:
            print("{}.  {}".format(iterators.index(i) + 1, i))



pancake_house_menu = PancakeHouseMenu()
lunch_house_menu = LunchMenu()
dinner_house_menu = CafeMenu()

waitress = Waitress(pancake_house_menu, lunch_house_menu, dinner_house_menu)
waitress.printMenu()
