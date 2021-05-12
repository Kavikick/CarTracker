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
