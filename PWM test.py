#PWM test
import RPi.GPIO as GPIO
from time import sleep

SpeedPin = 12
DirectionPin = 4

GPIO.cleanup()
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BCM)	#set pin numbering system
GPIO.setup(SpeedPin,GPIO.OUT)
GPIO.setup(DirectionPin,GPIO.OUT)

pi_pwm = GPIO.PWM(SpeedPin,1000)		#create PWM instance with frequency
pi_pwm.start(0)
GPIO.output(DirectionPin, True)

#start PWM of required Duty Cycle 
while True:
    for duty in range(0,101,1):
        pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
        sleep(0.1)
    for duty in range(100,0,-1):
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.1)