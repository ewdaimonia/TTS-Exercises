# Control Flow Exercises 2
# By Gabriel Smith
import re


def passwordChecker(password):
    # DISCLAIMER: I'm very bad with regex, I very obviously copied this from a regex generator.
    if(re.match(r'(?=[A-Za-z0-9@#$%^&+!=]+$)^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+!=])(?=.{6,16})', password)):
        print("Your password passes")
        return True
    else:
        print("Your password shall not pass")
        return False


def main():
    print("Please create a password with 1 uppercase character, 1 lowercase character, 1 symbol, and with a length between 6-16.")
    while(not passwordChecker(input("Please enter a password to see if it passes: "))):
        print("Please try again. ")


if __name__ == "__main__":
    main()
