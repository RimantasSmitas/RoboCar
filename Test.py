<<<<<<< HEAD
import RPi.GPIO as gpio
=======
import rpi.gpio as gpio
>>>>>>> 9d4a5ec2fdc1ede680ed4ff3a1a3e90119b5c633

import time


PWMF1 = 2
PWMF2 = 3

FrontLeft = 17
FrontRight = 27


gpio.setwarnings(False)
gpio.cleanup()

gpio.setmode(gpio.BCM)

gpio.setup(PWMF1, gpio.OUT)
gpio.setup(PWMF2, gpio.OUT)
gpio.setup(FrontLeft, gpio.OUT)
gpio.setup(FrontRight, gpio.OUT)


gpio.output(PWMF1, True)

gpio.output(FrontLeft, True)

gpio.output(PWMF2, True)

gpio.output(FrontRight, True)

time.sleep(0.5)

gpio.output(FrontLeft, False)

gpio.output(FrontRight, False)

time.sleep(0.5)

gpio.output(PWMF1, False)
gpio.output(PWMF2, False)
