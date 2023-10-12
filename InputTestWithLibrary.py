from sshkeyboard import listen_keboard

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
    listen_keboard(on_press = press)