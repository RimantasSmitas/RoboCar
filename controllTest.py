import RPi.GPIO as GPIO
from time import sleep
from sshkeyboard import listen_keyboard 
# PWM pins

PWMPin1 = 13
PWMPin2 = 19
PWMPin3 = 12
PWMPin4 = 18

# Direction pins

DirPin1 = 4
DirPin2 = 3
DirPin3 = 15
DirPin4 = 14

Speed = 50

#Set up GPIO
GPIO.cleanup()
GPIO.setwarnings(False) #disable warnings
GPIO.setmode(GPIO.BCM)  #set pin numbering system

#Set up pins
GPIO.setup(PWMPin1,GPIO.OUT)
GPIO.setup(PWMPin2,GPIO.OUT)
GPIO.setup(PWMPin3,GPIO.OUT)
GPIO.setup(PWMPin4,GPIO.OUT)

GPIO.setup(DirPin1,GPIO.OUT)
GPIO.setup(DirPin2,GPIO.OUT)
GPIO.setup(DirPin3,GPIO.OUT)
GPIO.setup(DirPin4,GPIO.OUT)

Speed1 = GPIO.PWM(PWMPin1,1000)         #create PWM instance with frequency
Speed2 = GPIO.PWM(PWMPin2,1000)         #create PWM instance with frequency
Speed3 = GPIO.PWM(PWMPin3,1000)         #create PWM instance with frequency
Speed4 = GPIO.PWM(PWMPin4,1000)         #create PWM instance with frequency

Speed1.start(0)
Speed2.start(0)
Speed3.start(0)
Speed4.start(0)


GPIO.output(DirPin1,False)
GPIO.output(DirPin2, True)
GPIO.output(DirPin3, False)
GPIO.output(DirPin4, True)

def TurnLeft():
    GPIO.output(DirPin1,False)
    GPIO.output(DirPin2, True)
    GPIO.output(DirPin3, True)
    GPIO.output(DirPin4, False)
    Speed1.ChangeDutyCycle(Speed)
    Speed2.ChangeDutyCycle(Speed)
    Speed3.ChangeDutyCycle(Speed)
    Speed4.ChangeDutyCycle(Speed)
    print("Turning Left")
    
def TurnRight():
    print("Turning Right")
    
    GPIO.output(DirPin1,True)
    GPIO.output(DirPin2, False)
    GPIO.output(DirPin3, False)
    GPIO.output(DirPin4, True)
    Speed1.ChangeDutyCycle(Speed)
    Speed2.ChangeDutyCycle(Speed)
    Speed3.ChangeDutyCycle(Speed)
    Speed4.ChangeDutyCycle(Speed)

def GoForward():
    GPIO.output(DirPin1,False)
    GPIO.output(DirPin2, True)
    GPIO.output(DirPin3, False)
    GPIO.output(DirPin4, True)
    Speed1.ChangeDutyCycle(Speed)
    Speed2.ChangeDutyCycle(Speed)
    Speed3.ChangeDutyCycle(Speed)
    Speed4.ChangeDutyCycle(Speed)
    print("Going Forward")

def GoBackward():
    GPIO.output(DirPin1,True)
    GPIO.output(DirPin2, False)
    GPIO.output(DirPin3, True)
    GPIO.output(DirPin4, False)
    Speed1.ChangeDutyCycle(Speed)
    Speed2.ChangeDutyCycle(Speed)
    Speed3.ChangeDutyCycle(Speed)
    Speed4.ChangeDutyCycle(Speed)
    print("reversing")

def IncreaseSpeed():
    global Speed
    Speed+=10
    print(Speed)

def DecreaseSpeed():
    global Speed
    Speed-=10
    print(Speed)

def Stop():
    Speed1.ChangeDutyCycle(0)
    Speed2.ChangeDutyCycle(0)
    Speed3.ChangeDutyCycle(0)
    Speed4.ChangeDutyCycle(0)

def press(key):
    if key == "w":
       GoForward()  
    if key == "s":
       GoBackward() 
    if key == "a":
       TurnLeft() 
    if key == "d":
       TurnRight() 
    if key == "i":
       IncreaseSpeed()
    if key == "k":
       DecreaseSpeed()
    if key == "b":
       Stop()
        

while True:
    listen_keyboard(on_press = press)
