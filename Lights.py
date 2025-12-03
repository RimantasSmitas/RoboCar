import RPi.GPIO as GPIO
from time import sleep
from enum import Enum

Light1 = 5
Light2 = 6
Light3 = 17
Light4 = 22
Light5 = 23
Light6 = 24
Light7 = 25
Light8 = 27


#Set up GPIO
GPIO.cleanup()
GPIO.setwarnings(False) #disable warnings
GPIO.setmode(GPIO.BCM)  #set pin numbering system

#Set up pins
GPIO.setup(Light1,GPIO.OUT)
GPIO.setup(Light2,GPIO.OUT)
GPIO.setup(Light3,GPIO.OUT)
GPIO.setup(Light4,GPIO.OUT)

GPIO.setup(Light5,GPIO.OUT)
GPIO.setup(Light6,GPIO.OUT)
GPIO.setup(Light7,GPIO.OUT)
GPIO.setup(Light8,GPIO.OUT)

class Lights(Enum):
    Light1 = 1 
    Light2 = 2
    Light1 = 3 
    Light2 = 4
    Light1 = 5 
    Light2 = 6
    Light1 = 7 
    Light2 = 8

Lights.