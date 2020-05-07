# Data Structures Exercises 4
# By Gabriel Smith


def main():
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {'Zach': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}
    rollNumber = list(filter(lambda i: i in sampleDict.values(), rollNumber))
    print(rollNumber)


if __name__ == "__main__":
    main()
