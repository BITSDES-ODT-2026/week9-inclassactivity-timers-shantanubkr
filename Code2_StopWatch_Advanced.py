#Code for Advanced StopWatch
from machine import Pin
import time
import random

# Define basic values
pb1 = Pin(18, Pin.IN, Pin.PULL_UP)
pb2 = Pin(19, Pin.IN, Pin.PULL_UP)
led = Pin(14, Pin.OUT)
start = None
timer = False
last_lap_time = None

# System Behavior:
while True:
    # Initialise
    starter = pb1.value()
    stopper = pb2.value()

    # Button 1 (PB1): First press → Starts the timer. Subsequent presses → Records a lap time and prints the time since the previous lap.
    if starter == 0:
        time.sleep(0.2)
        if start is None:
            start = time.ticks_ms()
            last_lap_time = start
            timer = True
            print("Timer Started!")

            while pb1.value() == 0:
                pass

        else:
            while pb1.value() == 0:
                pass
            time.sleep(0.1)
            current = time.ticks_ms()
            lap = time.ticks_diff(current, last_lap_time)
            last_lap_time = current
            print("this lap was ", lap / 1000, "seconds long")

    # Button 2 (PB2): If the timer has not started → Display "Timer not Started". If the timer is running → Stop the timer and display the total elapsed time, then reset the system.
    if stopper == 0:
        time.sleep(0.2)
        if timer == False:
            print("Timer not started")
        elif timer == True:
            timer = False
            end = time.ticks_ms()
            elapsed = time.ticks_diff(end, start)
            print("Timer Stopped")
            print("Total time elapsed = ", elapsed / 1000 , "seconds")
            start = None
            last_lap_time = None

    time.sleep(0.1)
