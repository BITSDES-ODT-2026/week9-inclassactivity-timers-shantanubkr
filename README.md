[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/wLqdLPm0)
**Code 2 : Build a Lap Timer using Push Buttons** 
In this activity, you will develop a lap timer system using two push buttons and the time.ticks_ms() function in MicroPython.


**System Behavior:**

Button 1 (PB1):
First press → Starts the timer.
Subsequent presses → Records a lap time and prints the time since the previous lap.

Button 2 (PB2):
If the timer has not started → Display "Timer not Started".
If the timer is running → Stop the timer and display the total elapsed time, then reset the system.

Help & Hints:
Use time.ticks_ms() for time measurement.
Use time.ticks_diff() to calculate time differences.
Maintain a lap counter.

**Your program should continuously monitor the buttons and print the lap time and total elapsed time in milliseconds to the serial console.**


**Code 3 : Button Press Frequency Counter**

Objective:
Measure how many times a button is pressed in 5 seconds.

**Code Operation:**
Start counting when the first button press occurs. (Use an Indicicator to start)
A 5-second timer begins using time.ticks_ms().
Count how many presses occur within that period. (Use an Indicator to end)

After 5 seconds:
Print the total count.
