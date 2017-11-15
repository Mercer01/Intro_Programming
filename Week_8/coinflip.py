import random


def getInputs():
    while True:
        inputs = input("How many times do you want to flip the coin:")
        if inputs.isnumeric():
            return int(inputs)
        print("Incorrect values please try again")


def simulateFlips(count):
    flips = []
    for x in range(count):
        flips.append(random.randint(0, 1))
    return flips


def displayResults(results):
    head_count = results.count(0) / 100
    tail_count = results.count(1) / 100
    print("There were {0} heads and {1} tails".format(head_count, tail_count))


def main():
    count = getInputs()
    flips = simulateFlips(count)
    displayResults(flips)


if __name__ == '__main__':
    main()
