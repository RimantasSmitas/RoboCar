import RPi.GPIO as GPIO
import time
from time import sleep



A = 2




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()



while True:
   GPIO.setmode(A,GPIO.Out)
   GPIO.output(A,True)
   sleep(0.00001)
   GPIO.setmode(A,GPIO.In)
   timest = time.time_ns()

   while (GPIO.input(5)==True and (time_ns() - timest < 3000));
   timeCalc = time_ns() - timest 
    
   print("Sensor A")

   print(timeCalc)
   sleep(1)
   