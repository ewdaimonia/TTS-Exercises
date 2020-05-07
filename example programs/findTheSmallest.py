# The purpose of this code is to swap one digit in a multi digit integer
# in order to create a new number to make the final number as small as possible
# with the limitaion of only swapping two digits.
import functools

# this is a function that should take a list and the indexes of the two digits
# to swap as params and then return the new list with those numbers swapped at
# those indexes


def change(num, s, t):
    temp = num[t]
    num[t] = num[s]
    num[s] = temp
    res = functools.reduce(lambda total, d: 10 * total + d, num, 0)
    print("INNER TEST FOR PASSED IN VALUE: " + str(res))
    return res

# this is the main function that takes the int, turns it into a list
# then passes it into the change function and compares it with the
# currently smallest list


def smallest(n):
    nList = list(map(int, str(n)))
    smol = nList.index(min(nList))
    target = 0
    for i in range(1, len(nList), 1):
        # The next line is my work around for this problem
        #testList = nList.copy()
        if(int(change(nList, smol, i)) < int(change(nList, smol, target))):
            target = i
            print("TEST VALUE FOR iterator: " + str(i))
            print("TEST VALUE FOR GLOBAL nList: " + str(nList))
    print("Final result set: ")
    print([int(change(nList, smol, target)), smol, target])
    return [int(change(nList, smol, target)), smol, target]


def main():
    smallest(261235)


if __name__ == "__main__":
    main()
