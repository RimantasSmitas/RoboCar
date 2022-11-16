import RPi.GPIO as GPIO


A = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(A,GPIO.IN)


while True:
    print GPIO.input(A)
