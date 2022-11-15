import RPi.GPIO as GPIO
from time import sleep



A = 2




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


GPIO.setup(A, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)


while True:
   print("Sensor A")

   print(GPIO.input(A))
   sleep(1)
