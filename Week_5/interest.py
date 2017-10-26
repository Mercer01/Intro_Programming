#-------------------------------------------------------------------------------
# interest.py - an example use of functions
# Matthew Poole
#-------------------------------------------------------------------------------

def calcFutureValue(amount, years):
    interestRate = 0.055
    for year in range(years):
        amount = amount * (1 + interestRate)
    return amount 

def futureValue():
    amount = eval(input("Enter an amount to invest: "))
    years = eval(input("Enter the number of years: "))
    finalValue = calcFutureValue(amount, years)
    print("Investing GBP {0:0.2f} for {1} years".format(amount, years), 
          "will result in GBP {0:0.2f}.".format(finalValue))
