from abc import ABC, abstractmethod


class QuackObservable:
    def registerObserver(self):
        pass

    def notifyObservers(self):
        pass


class Observable(QuackObservable):
    def __init__(self) -> None:
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def notifyObservers(self, duck):
        for observer in self.observers:
            observer.update(duck)


class Observer:
    def update(self, duck):
        pass


class Quackologist(Observer):
    def update(self, duck):
        if duck.name != "Flock":
            print('Quackologist: {} just quacked'.format(duck.name))


class Quackable(ABC, Observable):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def quack(self):
        pass


class MallardDuck(Quackable):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Mallard duck'

    def quack(self):
        print('Quack')


class ReadheadDuck(Quackable):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Red head duck'

    def quack(self):
        print("Quack")


class DuckCall(Quackable):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Duck Call'

    def quack(self):
        print('Kwak')


class RubberDuck(Quackable):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Rubber duck'

    def quack(self):
        print('Squeak')


class Goose:
    def honk(self):
        print('Honk')


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose) -> None:
        self.goose = goose
        self.name = "Goosse"

    def quack(self):
        self.goose.honk()


class QuackCounter(Quackable):
    numOfQuacks = 0

    def __init__(self, duck: Quackable) -> None:
        self.duck = duck
        self.name = duck.name

    def quack(self):
        self.duck.quack()
        QuackCounter.numOfQuacks += 1

    @classmethod
    def getQuacks(cls):
        return cls.numOfQuacks


class AbstractDuckFactory(ABC):
    @abstractmethod
    def createMallardDuck(self):
        pass

    @abstractmethod
    def createRedheadDuck(self):
        pass

    @abstractmethod
    def createDuckCall(self):
        pass

    @abstractmethod
    def createRubberDuck(self):
        pass


class CountingDuckFactory(AbstractDuckFactory):

    def createMallardDuck(self):
        return QuackCounter(MallardDuck())

    def createRedheadDuck(self):
        return QuackCounter(ReadheadDuck())

    def createDuckCall(self):
        return QuackCounter(DuckCall())

    def createRubberDuck(self):
        return QuackCounter(RubberDuck())


class Flock(Quackable):
    def __init__(self) -> None:
        super().__init__()
        self.quackers = []
        self.name = "Flock"

    def add(self, quacker):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()
            self.notifyObservers(quacker)


class DuckSimulator:
    duckfactory = CountingDuckFactory()

    def simulate(self):
        redheadDuck = DuckSimulator.duckfactory.createRedheadDuck()
        duckcall = DuckSimulator.duckfactory.createDuckCall()
        rubberduck = DuckSimulator.duckfactory.createRubberDuck()
        gooseDuck = GooseAdapter(Goose())

        print('\nDuck Simulator: with composite - Flocks')

        flockOfDucks = Flock()

        flockOfDucks.add(redheadDuck)
        flockOfDucks.add(duckcall)
        flockOfDucks.add(rubberduck)
        flockOfDucks.add(gooseDuck)

        flockofMallard = Flock()
        flockOfDucks.add(flockofMallard)

        mallardone = DuckSimulator.duckfactory.createMallardDuck()
        mallardtwo = DuckSimulator.duckfactory.createMallardDuck()
        mallardthree = DuckSimulator.duckfactory.createMallardDuck()
        mallardfour = DuckSimulator.duckfactory.createMallardDuck()

        flockofMallard.add(mallardone)
        flockofMallard.add(mallardthree)
        flockofMallard.add(mallardfour)
        flockofMallard.add(mallardtwo)

        # flockOfDucks.add(flockofMallard)

        quackologist = Quackologist()
        flockOfDucks.registerObserver(quackologist)
        flockofMallard.registerObserver(quackologist)

        print('\nDuck Simulator: Whole Flock simulation')
        self.simulateone(flockOfDucks)

        # print('\nDuck Simulator: Mallard Flock simulation')
        self.simulateone(flockofMallard)

        # self.simulateone(mallardduck)
        # self.simulateone(readheadDuck)
        # self.simulateone(duckcall)
        # self.simulateone(rubberduck)
        # self.simulateone(gooseDuck)

        print('{} quacks were counted'.format(QuackCounter.getQuacks()))

    def simulateone(self, duck: Quackable):
        duck.quack()


x = DuckSimulator()
x.simulate()
