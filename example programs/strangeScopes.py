# This file is meant to show how lists which are entered as params into functions in python will retain any changes that were made to the list within the function
# Which is untrue for any basic datatypes passed into functions such as int or string


def processInt(num):
    num *= 10
    num /= 3.14
    num += 65
    return num


def processList(eList):
    eList += [0, 10]
    eList += [0, 10]
    return eList


def main():
    numberOutside = 5
    print("First we'll show that an int which is passed into a function will not be altered by anything that happens within the body of the function.")
    print("Int outside of function and before passing into function: " +
          str(numberOutside))
    print("Return value from function after int is passed in and processed: " +
          str(processInt(numberOutside)))
    print("Original variable of int outside the function that we can see is unaltered by anything inside the function body: " + str(numberOutside))
    print(" ")
    print(" ")
    listOutside = [5, 0]
    print("Second we'll show that a list which is passed into a function WILL be altered by anything that happens within the body of the function.")
    print("List outside of function and before passing into function: " +
          str(listOutside))
    print("Return value from function after list is passed in and processed: " +
          str(processList(listOutside)))
    print("Original list outside the function that we can see IS altered by anything inside the function body: " + str(listOutside))

    print(" ")
    print("I am at a loss for why python would operate like this as there are mnay times I might want to see how a function will alter a list without altering the original list.")


if __name__ == "__main__":
    main()
