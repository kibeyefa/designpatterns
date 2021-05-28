from abc import ABCMeta, abstractmethod

class Duck:
    def __init__(self, flybehaviour, quackbehaviour) -> None:
        self._quackBehaviour = quackbehaviour
        self._flyBehaviour = flybehaviour

    def swim(self):
        pass

    def display(self):
        pass

    def performQuack(self):
        self._quackBehaviour.quackBehaviour(self)

    def performFly(self):
        self._flyBehaviour.flyBehaviour(self)

class FlyBehaviour(ABCMeta):
    """Declare an inferface common to all flying duck algorithms"""
    @abstractmethod
    def flyBehaviour(self):
        pass

class QuackBehaviour(ABCMeta):
    """Declare an inferface common to all quacking duck algorithms"""
    @abstractmethod
    def quackBehaviour(self):
        pass

class FlyWithWings(FlyBehaviour):
    """Flying algorithm with wings"""
    @abstractmethod
    def flyBehaviour(self):
        print("I fly with wings")

class FlyNoWay(FlyBehaviour):
    """Flying algorithm without wings"""
    @abstractmethod
    def flyBehaviour(self):
        print("I can't fly")

class Quack(QuackBehaviour):
    """Implements duck quacking"""
    @abstractmethod
    def quackBehaviour(self):
        print("I am a quacking duck")

class Squeak(QuackBehaviour):
    """Implements duck squeaking"""
    @abstractmethod
    def quackBehaviour(self):
        print("I am a squeaking duck")

class MuteQuack(QuackBehaviour):
    """Implements mute ducks"""
    @abstractmethod
    def quackBehaviour(self):
        print("Can't quack")


duck_1 = Duck(FlyNoWay, Squeak)
duck_1.performQuack(); duck_1.performFly()

