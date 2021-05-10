from robot import Robot

robot = Robot("maze3.txt")

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
        v = input("press enter to move to the next step")
        robot.printMaze()

navigateMaze()
print("Congratulations! You have solved the maze!")

