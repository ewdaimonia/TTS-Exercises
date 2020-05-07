# This is a little text based game I wrote in one of my first C++ classes.
# I edited it so it would run in python.


class Game:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.choice = 0
        self.candle = 0
        self.napTaken = 0

    def welcome(self):
        print(f'Welcome {self.name}, you awaken in a dark cave with little to no light other than an old candle which is poorly fastened to the wall.')

    def switcher(self):
        if(self.choice == 1):
            if(self.candle == 0):
                print(
                    "You rip the candle from the wall and now might be able to see into the darkness a bit easier.")
                self.score += 10
                self.candle = 1
            else:
                print("You already hold the candle.")
        if(self.choice == 2):
            if(self.candle == 1 & self.napTaken == 1):
                print("As you peer into the darkness, you notice a wild boar and because you have the candle, you are able to scare it with the flame momentarily.")
                print(
                    "While the boar is recovering from its minor flame fright, you are able to sprint past it and out of the cave!!")
                print("You have won the Cave Adventure!!")
                self.score += 5000
                self.choice = 4
            else:
                print(
                    "As you peer into the darkness, you hear some grunting and a wild boar pounces upon you!")
                print("You have no time to react and are slain by the evil beast.")
                print("You have died and have lost Cave Adventure.")
                self.score -= 5000
                self.choice = 4
        if(self.choice == 3):
            if(self.napTaken == 0):
                print(
                    "You decide you need more rest before you can explore the rest of the cave, you take a killer nap.")
                self.score += 50
                self.napTaken = 1
            else:
                print(
                    "You have already slept too much. Did you know sleeping too much is a symptom of seasonal affective disorder?")
                self.score -= 5
        if(self.choice == 4):
            print(f'Game over, {self.name}, you scored: {self.score}')
            self.choice = 4
        if(((self.choice) < 1) & (self.choice > 4)):
            print("That is not an option.")

    def menu(self):
        while(self.choice != 4):
            if(self.choice != 4):
                print("Cave Adventure Menu")
                print(f'Score: {self.score}')
                print("1. Take candle.")
                print("2. Peer into darkness.")
                print("3. Go back to sleep.")
                print("4. Quit.")
                print()
                self.choice = (int(input("What will you do? ")))
                self.switcher()
            else:
                print(f'Game over, {self.name}, you scored: {self.score}')
                break


def main():
    newGame = Game(input("Please enter your name: "))
    newGame.welcome()
    newGame.menu()


if __name__ == "__main__":
    main()
