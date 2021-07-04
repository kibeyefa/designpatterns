from abc import abstractmethod, ABC


# Create vendor classes
class Light:

    def __init__(self, location: str):
        self.__location = location

    def on(self):
        print(f"{self.__location} Light is on!")

    def off(self):
        print(f"{self.__location} Light is off!")

class GarageDoor:

    def up(self):
        print("Garage door is open")

    def down(self):
        print("Garage door is closed")

    def stop(self):
        pass

    def lightOn(self):
        pass

    def lightOff(self):
        pass

class CeilingFan:
    def __init__(self, location):
        self.__location = location

    def high(self):
        self.__speed = 100
        print(f"{self.__location} fan is set to high")

    def medium(self):
        self.__speed = 50
        print(f"{self.__location} fan is set to medium")

    def low(self):
        self.__speed = 25
        print(f"{self.__location} fan is set to low")

    def off(self):
        self.__speed = 0
        print(f"{self.__location} fan is off")

    def getSpeed(self):
        print(self.__speed)

class Stereo:
    pass


# Creating Command Objects
class Command(ABC):
    """Base class for all command objects"""

    def execute(self):
        pass

class LightOnCommand(Command):
    """Implements light on command objects"""

    def __init__(self, light: Light):
        self.__light = light

    def execute(self):
        self.__light.on()

class LightOffCommand(Command):
    """Implements light off command objects"""

    def __init__(self, light: Light):
        self.__light = light

    def execute(self):
        self.__light.off()

class GarageDoorOpenCommand(Command):

    def __init__(self, garageDoor: GarageDoor):
        self.__garagedoor = garageDoor

    def execute(self):
        self.__garagedoor.up()

class GarageDoorCloseCommand(Command):

    def __init__(self, garageDoor: GarageDoor):
        self.__garagedoor = garageDoor

    def execute(self):
        self.__garagedoor.down()

class CeilingFanHighCommand(Command):

    def __init__(self, fan: CeilingFan):
        self.__fan = fan

    def execute(self):
        self.__fan.high()

class CeilingFanMediumCommand(Command):

    def __init__(self, fan: CeilingFan):
        self.__fan = fan

    def execute(self):
        self.__fan.medium()

class CeilingFanLowCommand(Command):

    def __init__(self, fan: CeilingFan):
        self.__fan = fan

    def execute(self):
        self.__fan.low()

class CeilingFanOffCommand(Command):

    def __init__(self, fan: CeilingFan):
        self.__fan = fan

    def execute(self):
        self.__fan.off()


class SimpleRemoteControl:

    def __init__(self):
        self.slots = {1: [None, None], 2: [None, None], 3: [None, None], 4: [None, None], 5: [None, None], 6: [None, None], 7: [None, None]}

    def setCommand(self, slot: int, onCommand: Command, offCommand: Command):
        self.slots[slot][0] = onCommand
        self.slots[slot][1] = offCommand

    def buttonWasPressed(self, slot: int, index):
        self.slots[slot][index].execute()


class RemoteControlTest:

    @classmethod
    def main(cls):
        remote = SimpleRemoteControl()

        light = Light("Kitchen")
        mainFan = CeilingFan("Main")
        garageDoor = GarageDoor()

        lighton = LightOnCommand(light)
        lightoff = LightOffCommand(light)
        garageDooropen = GarageDoorOpenCommand(garageDoor)
        fanOnCommand = CeilingFanHighCommand(mainFan)

        remote.setCommand(1, lighton, lightoff)
        remote.setCommand(2, fanOnCommand, garageDooropen)
        remote.buttonWasPressed(1, 0)
        remote.buttonWasPressed(1, 1)
        remote.buttonWasPressed(2, 1)
        remote.buttonWasPressed(2, 0)

RemoteControlTest().main()
