# Control Flow Exercises 3
# By Gabriel Smith


def main():
    ages = []
    counter = 0
    while(len(ages) != 3):
        counter += 1
        ages.append(int(input(f"Please enter age {counter}: ")))
    print(ages)
    if(min(ages) == max(ages)):
        print("All the ages you entered were the same")
    elif(ages[0] == ages[1] or ages[1] == ages[2]):
        print("Two of the ages you entered were the same, but")
        print("The youngest age entered was " + str(min(ages)))
        print("The oldest age entered was " + str(max(ages)))
    else:
        print("The youngest age entered was " + str(min(ages)))
        print("The oldest age entered was " + str(max(ages)))


if __name__ == "__main__":
    main()
