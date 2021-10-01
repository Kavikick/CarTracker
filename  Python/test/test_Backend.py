from Backend import *
from datetime import timedelta


def test_Car():
    # init
    testCar = Car(1)
    assert testCar.number == 1
    assert testCar.lapsCompleted == 0
    assert testCar.time == timedelta()

    # Update
    # First lap
    time1 = timedelta(minutes=1, seconds=20)
    testCar.update(time1)
    assert testCar.lapsCompleted == 1
    assert testCar.time == time1
    assert testCar.laptimes[0] == time1

    # Second lap
    time2 = timedelta(minutes=2, seconds=30)
    difference = time2-time1
    testCar.update(time2)
    assert testCar.lapsCompleted == 2
    assert testCar.time == time2
    assert testCar.laptimes[1] == difference


def test_Tracker():
    # init
    testTracker = Tracker((2, 4, 9))
    referenceDict = {2: Car(2), 4: Car(4), 9: Car(9)}
    referenceList = [Car(2), Car(4), Car(9)]
    assert testTracker.cars == referenceDict
    assert testTracker.positions == referenceList

    # update
    timeCar9 = timedelta(minutes=1, seconds=20)
    testTracker.update(9, timeCar9)
    timeCar2 = timedelta(minutes=2, seconds=30)
    testTracker.update(2, timeCar2)
    referenceList = [Car(9), Car(2), Car(4)]
    assert testTracker.positions == referenceList
