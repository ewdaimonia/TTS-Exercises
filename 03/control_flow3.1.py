# Control Flow Exercises 1
# By Gabriel Smith
import random


def main():
    num = input("Please enter a random integer between 1 and 9: ")
    cont = 'y'
    numsToGuess = []
    for i in range(1, 10, 1):
        numsToGuess.append(i)
    while(cont == 'y'):
        try:
            guess = random.choice(numsToGuess)
        except:
            print(
                "You must've picked a number outside of the range I'm allowed to guess, goodbye.")
            break
        if(int(num) == guess):
            print("Your number is " + str(guess) + "!")
            print("Thanks for playing, goodbye!")
            cont = 'z'
        else:
            print("Your number was not " + str(guess))
            numsToGuess.remove(guess)
            cont = input("May I try again? (y/n)")
    if(cont == 'n'):
        print("Oh well, thanks for playing.")


if __name__ == "__main__":
    main()
