class Padlock(object):
    def __init_(self, combination):
        self.combination = combination
        self.isOpen = False

    def open(self, combination_entered):
        if self.isOpen:
            print("The lock is alread open")
        else:
            if self.combination != combination_entered:
                print("You entered the wrong combination")
            else:
                print("You opened the lock")
                self.isOpen = True

    def close(self):
        if self.isOpen:
            print("The lock is now closed")
            self.isOpen = False
        else:
            print("The lock is closed")

    def change_combination(self, newcombination):
        self.combination = newcombination
