from Backend import *
from datetime import timedelta


def test_Car():
    # init
    testCar = Car(1)
    assert testCar.number == 1
    assert testCar.lapsCompleted == 0
    assert testCar.time == timedelta()

    # Update
    time1 = timedelta(minutes=1, seconds=20)
    testCar.update(time1)
    assert testCar.lapsCompleted == 1
    assert testCar.time == time1
    assert testCar.laptimes[0] == time1

    time2 = timedelta(minutes=2, seconds=30)
    difference = time2-time1
    testCar.update(time2)
    assert testCar.lapsCompleted == 2
    assert testCar.time == time2
    assert testCar.laptimes[1] == difference
