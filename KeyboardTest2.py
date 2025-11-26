import RPi.GPIO as GPIO
from time import sleep
from sshkeyboard import listen_keyboard 
# PWM pins

PWMPin1 = 13
PWMPin2 = 19
PWMPin3 = 12
PWMPin4 = 18

f = 0
b = 0
r = 0
l = 0

# Direction pins

DirPin1 = 4
DirPin2 = 3
DirPin3 = 15
DirPin4 = 14

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

def press(key):
    global f,b,r,l
    if key == "w":
        f = 1
    if key == "s":
        b = 1
    if key == "a":
        l = 1
    if key == "d":
        r = 1
    print("Foward is", f,"Backwords is",b,"Right is",r,"Left is",l)
def release(key):
    global f,b,r,l
    if key == "w":
        f = 0
    if key == "s":
        b = 0
    if key == "a":
        l = 0
    if key == "d":
        r = 0
    print("Foward is", f,"Backwords is",b,"Right is",r,"Left is",l)
while True:
    listen_keyboard(on_press = press, on_release=release, sequential=True)
    print("Foward is", f,"Backwords is",b,"Right is",r,"Left is",l)
