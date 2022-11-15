import RPi.GPIO as GPIO
import time
from time import sleep

A = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
   GPIO.setup(A,GPIO.Out)
   GPIO.output(A,True)
   sleep(0.00001)
   GPIO.setup(A,GPIO.In)
   timest = time.time_ns()

   while (GPIO.input(A)==True and (time_ns() - timest < 3000))
      timeCalc = time_ns() - timest 
      print("Sensor A")
      print(timeCalc)
      sleep(1)
   