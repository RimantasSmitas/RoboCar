import RPi.GPIO as GPIO
import time




A = 13
B = 6 




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


GPIO.setup(A, GPIO.IN)
GPIO.setup(B, GPIO.IN)


while True:
   print("Sensor A")
   print(GPIO.input(A))
   print("Sensor B")
   print(GPIO.input(B)