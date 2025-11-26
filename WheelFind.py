import RPi.GPIO as GPIO
from time import sleep

# PWM pins

PWMPin1 = 2
PWMPin2 = 17
PWMPin3 = 14
PWMPin4 = 23

# Direction pins

DirPin1 = 4
DirPin2 = 3
DirPin3 = 15
DirPin4 = 18

#Set up GPIO
GPIO.cleanup()
GPIO.setwarnings(False)	#disable warnings
GPIO.setmode(GPIO.BCM)	#set pin numbering system

#Set up pins
GPIO.setup(PWMPin1,GPIO.OUT)
GPIO.setup(PWMPin2,GPIO.OUT)
GPIO.setup(PWMPin3,GPIO.OUT)
GPIO.setup(PWMPin4,GPIO.OUT)

GPIO.setup(DirPin1,GPIO.OUT)
GPIO.setup(DirPin2,GPIO.OUT)
GPIO.setup(DirPin3,GPIO.OUT)
GPIO.setup(DirPin4,GPIO.OUT)

Speed1 = GPIO.PWM(PWMPin1,1000)		#create PWM instance with frequency
Speed2 = GPIO.PWM(PWMPin2,1000)		#create PWM instance with frequency
Speed3 = GPIO.PWM(PWMPin3,1000)		#create PWM instance with frequency
Speed4 = GPIO.PWM(PWMPin4,1000)		#create PWM instance with frequency

Speed1.start(0)
Speed2.start(0)
Speed3.start(0)
Speed4.start(0)


GPIO.output(DirPin1,False)
GPIO.output(DirPin2, True)
GPIO.output(DirPin3, False)
GPIO.output(DirPin4, True)
while True:
	for duty in range(25,50,1):
		Speed1.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel1")
		sleep(0.1)

	for duty in range(50,25,-1):
		Speed1.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel1")
		sleep(0.1)

	for duty in range(25,50,1):
		Speed2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel2")
		sleep(0.1)

	for duty in range(50,25,-1):
		Speed2.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel2")
		sleep(0.1)

	for duty in range(25,50,1):
		Speed3.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel3")
		sleep(0.1)

	for duty in range(50,25,-1):
		Speed3.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel3")
		sleep(0.1)

	for duty in range(25,50,1):
		Speed4.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel4")
		sleep(0.1)

	for duty in range(50,25,-1):
		Speed4.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
		print("Wheel4")
		sleep(0.1)
