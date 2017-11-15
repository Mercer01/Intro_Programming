#-------------------------------------------------------------------------------
# tennis.py - a program to illustrate simulation and program design
#-------------------------------------------------------------------------------


def main():
    prWinPt, num_Sets = getInputs()

    wins_sets = simulateNGames(prWinPt, num_Sets)
    printSummary(wins_sets, num_Sets)


def getInputs():
    prWinPt = eval(input("Prob. of winning a point: "))
    numSets = int(input("how many sets of tennis should be played?:"))
    return prWinPt, numSets


def simulateNGames(prWinPt, num_Sets):
    wins_op = 0
    wins = 0
    for x in range(num_Sets):
        pointsPl, pointsOp = simulateGame(prWinPt)
        if pointsPl > pointsOp:
            wins += 1
        elif pointsPl > pointsOp:
            wins_op += 1
    return wins


def simulateGame(prWinPt):
    from random import random
    pointsPl, pointsOp = 0, 0
    while not gameOver(pointsPl, pointsOp):
        if random() < prWinPt:
            pointsPl = pointsPl + 1
        else:
            pointsOp = pointsOp + 1
    return pointsPl, pointsOp


def gameOver(pointsPl, pointsOp):
    return (pointsPl >= 6 or pointsOp >= 6) and  \
        abs(pointsPl - pointsOp) >= 2


def printSummary(wins, num_Sets):
    proportion = wins / num_Sets
    print("Wins sets:", wins, end="  ")
    print("Proportion: {0:0.2f}".format(proportion))


if __name__ == '__main__':
    main()
