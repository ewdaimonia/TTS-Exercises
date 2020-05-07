# Data Structures Exercises 2
# By Gabriel Smith


def main():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    listThree = []
    for i in range(0, 7, 1):
        if(i % 2 != 0):
            listThree.append(listOne[i])
        if(i % 2 == 0):
            listThree.append(listTwo[i])
    print(listThree)


if __name__ == "__main__":
    main()
