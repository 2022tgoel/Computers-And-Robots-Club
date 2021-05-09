from robot import Robot

robot = Robot("maze2.txt")

robot.printMaze()

print("STARTING ALGORITHM")

def isLeftOpen():
    robot.turnLeft()
    leftOpen = robot.canMoveForward()
    robot.turnRight()
    return leftOpen
def isFrontOpen():
    return robot.canMoveForward()
def isRightOpen():
    robot.turnRight()
    rightOpen = robot.canMoveForward()
    robot.turnLeft()
    return rightOpen
def turnAround():
    robot.turnLeft()
    robot.turnLeft()

def navigateMaze():
    while not robot.isDone():
        if isLeftOpen():
            robot.turnLeft()
            robot.moveForward()
        elif isFrontOpen():
            robot.moveForward()
        elif isRightOpen():
            robot.turnRight()
        else:
            turnAround()
        robot.printMaze()
        v = raw_input("press enter to move to the next step")

navigateMaze()

