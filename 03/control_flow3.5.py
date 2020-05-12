# Control Flow Exercises 5
# By Gabriel Smith


def analyzer(number):
    if(number % 2 != 0):
        print("Weird")
    elif(2 <= number <= 5):
        print("Not weird")
    elif(6 <= number <= 20):
        print("Weird")
    elif(number > 20):
        print("Not weird")
    else:
        print("That number doesn't match any of my opinions about weird numbers")


def validator():
    number = input("Gimme an integer and I'll tell you what I think of it: ")
    try:
        return int(number)
    except:
        print("That's not an integer.")


def main():
    sentinel = "Hello"
    while(type(sentinel) is not int):
        sentinel = validator()
    analyzer(sentinel)


if __name__ == "__main__":
    main()
