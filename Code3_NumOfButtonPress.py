#Code here
from machine import Pin
import time

pb1 = Pin(21,Pin.IN,Pin.PULL_UP)
pb2 = Pin(19,Pin.IN,Pin.PULL_UP)
count = 0
start = None

while True:
    pb1_val = pb1.value()
    pb2_val = pb2.value()
    
    
    if pb2_val == 0 and count == 0:
        start = time.ticks_ms()
        count = count + 1
        time.sleep(0.2)
    
    elif pb2_val == 0:
        if count > 0: 
            count = count + 1
            print(count - 1)
            time.sleep(0.2)
        
    if start is not None and time.ticks_diff(time.ticks_ms(), start) >= 5000:
        print("Final Count:", count-1)
        count = 0
        start = None
        print("Resetting...")
