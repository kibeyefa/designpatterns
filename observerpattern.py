from abc import ABC, abstractmethod

def average(array):

    def sum(array):
        sum = 0
        for i in array:
            sum += i
        return sum

    sum = sum(array)
    average = sum / len(array)
    return average

class Observer(ABC):

    @abstractmethod
    def update(self, temperature, pressure, humidity):
        pass

class DisplayElement(ABC):

    @abstractmethod
    def display(self):
        pass

class Subject(ABC):

    @abstractmethod
    def registerObeserver(self, observer):
        pass

    @abstractmethod
    def removeObeserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class WeatherData(Subject):

    def __init__(self):
        self.observers = []

    def registerObeserver(self, observer):
        self.observers.append(observer)

    def removeObeserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        pass

    def measurementsChanged(self, temperature, pressure, humidity):
        for observer in self.observers:
            observer.update(temperature, pressure, humidity)

class CurrentConditionDisplay(Observer, DisplayElement):

    def update(self, temperature, pressure, humidity):
        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

    def display(self):
        print("----------------------------------------------------------------------------")
        print(f"The current temperature is {self.temperature}, pressure is {self.pressure}, humidity is {self.humidity}")
        print("----------------------------------------------------------------------------")

class StatisticsDisplay(Observer, DisplayElement):

    def __init__(self):
        self.temperatures = []
        self.humidities = []
        self.pressures = []

    def update(self, temperature, pressure, humidity):
        self.temperatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)

    def display(self):
        print("----------------------------------------------------------------------------")
        print(f"The minimum temperature is {min(self.temperatures)}, minimum humidity is {min(self.humidities)}, minimum pressure is {min(self.pressures)}")
        print(f"The maximum temperature is {max(self.temperatures)}, maximum humidity is {max(self.humidities)}, maximum pressure is {max(self.pressures)}")
        print(f"The average temperature is {average(self.temperatures)}, average humidity is {average(self.humidities)}, average pressure is {average(self.pressures)}")
        print("----------------------------------------------------------------------------")

class ThirdPartyDisplay(Observer, DisplayElement):

    def update(self, temperature, pressure, humidity):
        pass

    def display(self):
        pass

class ForecastDisplay(Observer, DisplayElement):

    def update(self, temperature, pressure, humidity):
        pass

    def display(self):
        pass

observer_1 = CurrentConditionDisplay()
observer_2 = StatisticsDisplay()

WeatherCompany = WeatherData()
WeatherCompany.registerObeserver(observer_1)
WeatherCompany.registerObeserver(observer_2)
WeatherCompany.measurementsChanged(120, 60, 89)
WeatherCompany.measurementsChanged(38, 67, 9)
WeatherCompany.measurementsChanged(4, 40, 49)
WeatherCompany.notifyObservers()

observer_1.display()
observer_2.display()