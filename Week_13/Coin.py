class Coin(object):
    def __init__(self, value):
        self.value = value

    def flip(self):
        self.flip_value = random.randint(0, 1)
        if self.flip_value == 0:
            print("Heads")
        else:
            print("Tails")


# pence = Coin("50p")
# pence.flip()
