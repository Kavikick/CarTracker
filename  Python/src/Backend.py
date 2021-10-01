'''
Car and Tracker classes for managing positions
'''
from datetime import timedelta


class Car:
    def __init__(self, number):
        self.number = number
        self.lapsCompleted = 0
        self.time = timedelta()
        self.laptimes = []

    def update(self, newtime):
        difference = newtime - self.time
        self.laptimes.append(difference)
        self.lapsCompleted += 1
        self.time = newtime

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.number == other.number
        else:
            return False


class Tracker:
    def __init__(self, cars=()):
        self.createCars(cars)

    def createCars(self, carNums):
        self.cars = {}
        self.positions = []
        for carNum in carNums:
            car = Car(carNum)
            self.cars[carNum] = car
            self.positions.append(car)

    def update(self, car, time):
        self.cars[car].update(time)
        # sort the list since that is the postions
