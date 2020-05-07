# Python Basics Practice assignment 2
# By Gabriel Smith

n = int(input("Please enter a single digit integer: "))
if (n > 9 | n < 1):
    print("That is not a single digit integer, goodbye")
else:
    finalNum = (n + (n*10+n) + (n*100 + n*10 + n))
    print(finalNum)
