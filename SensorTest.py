import RPi.GPIO as GPIO
import time




A = 6




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


GPIO.setup(A, GPIO.IN)


while True:
   print("Sensor A")
   print(GPIO.input(A))