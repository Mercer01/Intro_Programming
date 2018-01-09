import math
import random


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        self.area_circle = self.width * self.height
        return self.area_circle

    def perimeter(self):
        self.perimeter_circle = (self.width * 2) + (self.height * 2)
        return self.perimeter_circle

    def diagonal(self):
        self.diagonal_circle = math.sqrt(
            (self.height ** 2) + (self.width ** 2))
        return self.diagonal_circle

# Testing Rectangle total area
# rect = Rectangle(100, 100)

# print(rect.area())
# print(rect.perimeter())
# print(rect.diagonal())


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


class Book:
    def __init__(self, title, author, number_of_pages, ISBN, price, number_of_copies):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.ISBN = ISBN
        self.price = price
        self.number_of_copies = number_of_copies

    def update_price(self, price):
        self.price = price

    def sell_book(self):
        if self.number_of_copies <= 0:
            print("Invalid as we have 0 copies")
        else:
            self.number_of_copies -= 1

    def restock(self, new_number_of_books):
        self.number_of_copies += new_number_of_books
        print("We now have {0}, of the book {1}".format(
            self.number_of_copies, self.title))


# Bob_Joe_book = Book("Bob Johnson", "Bob", 300, "PN193041", 1.00, 50)
# Bob_Joe_book.update_price(5.00)
# Bob_Joe_book.sell_book()
# Bob_Joe_book.restock(50)
