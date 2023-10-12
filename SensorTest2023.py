# Include the library files
import RPi.GPIO as GPIO
from time import sleep

# Enter the button pins
LineSensorA = 5
LineSensorB = 6

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the pins as Input pins
GPIO.setup(LineSensorA,GPIO.IN)
GPIO.setup(LineSensorB,GPIO.IN)


while True:
    if GPIO.input(LineSensorA) == 1:
        print ("A is triggered")

    if GPIO.input(LineSensorB) == 1:
        print ("B is triggered")
