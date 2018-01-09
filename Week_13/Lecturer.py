class Lecturer():
    def __init__(self, firstname, lastname, salary, units_taught):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.units_taught = units_taught

    def addUnit(self):
        self.new_unit = input("Please enter the name of the new unit:")

        if self.new_unit in self.units_taught:
            print("The lecturer already teaches this unit")
        else:
            self.units_taught.append(self.new_unit)

        print("The lecturer {0}, teaches the units {1}".format(
            self.firstname + " " + self.lastname, self.units_taught))

    def removeUnit(self):
        print("The lecturer {0}, currently teaches the units {1}".format(
            self.firstname + " " + self.lastname, self.units_taught))
        self.old_unit = input("Please enter the name of the unit to remove:")

        if self.old_unit not in self.units_taught:
            print("Invalid input this unit is not taught by this lecterer")
        else:
            self.units_taught.remove(self.old_unit)

    def pay_rise(self):
        self.new_pay = input(
            "Please enter a the new pay for {0}:".format(self.firstname))

        if self.new_pay.isnumeric():
            self.new_pay = int(self.new_pay)
            if self.new_pay > self.salary:
                self.salary = self.new_pay

            else:
                print(
                    "The old salary is higher than the new one this is not a pay raisse")
        else:
            print("The value you entered is not a number")


# bobJoe = lecturer("Bob", "Joe", 50000, [
#     "INTPROG", "INDADD", "How to teach 101"])
# bobJoe.removeUnit()
# bobJoe.addUnit()
# bobJoe.pay_rise()
