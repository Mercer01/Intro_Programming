class Book():
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
