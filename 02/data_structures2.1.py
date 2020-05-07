# Data Structures Exercises 1
# By Gabriel Smith


def main():
    list1 = list(
        map(int, input("Please enter a list of space separated integers: ").split()))
    tuple1 = tuple(list1)
    print(hash(tuple1))
    # print(tuple1)


if __name__ == "__main__":
    main()
