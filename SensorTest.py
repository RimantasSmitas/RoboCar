import RPi.GPIO as GPIO
import time



A = 2




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


GPIO.setup(A, GPIO.IN)


while True:
   print("Sensor A")

   print(GPIO.input(A))


   GpioPinDigitalInput myButton = gpio.provisionDigitalInputPin(2, PinPullResistance.PULL_UP);
   print("Sensor Ab")
   print(myButton)
