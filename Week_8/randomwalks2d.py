import random
import math


def distanceBetweenFourPoints(x1, x2, y1, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def getInputs():
    numWalks = eval(input("How many random walks to take? "))
    numSteps = eval(input("How many steps for each walk? "))
    return numWalks, numSteps


def takeWalks(numWalks, numSteps):
    totalSteps = 0
    for walk in range(numWalks):
        stepsAway = takeAWalk(numSteps)
        totalSteps = totalSteps + stepsAway
    return totalSteps / numWalks


def takeAWalk(numSteps):
    Pos = [0, 0]
    for step in range(numSteps):
        num_rand = random.randint(0, 3)
        if num_rand == 0:
            Pos[0] += 1
        elif num_rand == 1:
            Pos[1] += 1
        if num_rand == 2:
            Pos[0] -= 1
        else:
            Pos[1] -= 1
    return abs(distanceBetweenFourPoints(0, Pos[0], 1, Pos[1]))


def printExpectedDistance(averageSteps):
    print("The expected number of steps away from the", end=" ")
    print("start point is", averageSteps)


def main():
    numWalks, numSteps = getInputs()
    averageSteps = takeWalks(numWalks, numSteps)
    printExpectedDistance(int(averageSteps))


if __name__ == '__main__':
    main()
