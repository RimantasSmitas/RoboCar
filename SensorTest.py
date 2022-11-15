import RPi.GPIO as GPIO
import time
from time import sleep

A = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

while True:
   GPIO.setup(A,GPIO.OUT)
   GPIO.output(A,True)
   sleep(0.00001)
   GPIO.setup(A,GPIO.IN)
   timest = time.time_ns()
   while (GPIO.input(A)==True and (time.time_ns() - timest < 3000)):
      timeCalc = time.time_ns() - timest 
      print("Sensor A")
      print(timeCalc)
      sleep(1)
   