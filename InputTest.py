
def TurnLeft():
    print("Turning Left")

def TurnRight():
    print("Turning Right")

def GoForward():
    print("Going Forward")

def GoBackward():
    print("reversing")

    
while True:
    value = input()
    if value == "w":
        GoForward()
    if value == "s":
        GoBackward()
    if value == "a":
        TurnLeft()
    if value == "d":
        TurnRight()