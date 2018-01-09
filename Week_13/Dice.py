class Dice():
    def __init__(self):
        self.sides_of_die = []
        self.value = None
        self.rand_value = None
        self.choice = None
        while True:
            self.value = input(
                "Please enter a value for the side of the dice, when done leave blank:")
            if self.value == "":
                break
            self.sides_of_die.append(self.value)

    def roll(self):
        self.rand_value = random.randint(0, len(self.sides_of_die))
        self.choice = self.sides_of_die[self.rand_value]
        print("Out of the possible values you rolled {0}".format(self.choice))


# die = Dice()
# die.roll()
