# -------------------------------------------------------------------------------
# readstrings.py - A demonstration of while loops to validate user input
# -------------------------------------------------------------------------------


# (note the need for "len(string) == 0" to appear twice).
def getString1():
    string = ""
    while len(string) == 0:
        string = input("Enter a non-empty string: ")
        if len(string) == 0:
            print("You didn't enter anything!")
    return string


# The same validation example, this time using the
# loop-and-a-half pattern.
def getString2():
    while True:
        string = input("Enter a non-empty string: ")
        if len(string) > 0:
            break
        print("You didn't enter anything!")
    return string
