#Run this command to install library
# sudo apt install python3-pip
##python3 -m pip install sshkeyboard --break-system-packages

from sshkeyboard import listen_keyboard

def TurnLeft():
    print("Turning Left")

def TurnRight():
    print("Turning Right")

def GoForward():
    print("Going Forward")

def GoBackward():
    print("reversing")

def press(key):
    if key == "w":
        GoForward()
    if key == "s":
        GoBackward()
    if key == "a":
        TurnLeft()
    if key == "d":
        TurnRight()


while True:
    listen_keyboard(on_press = press)
