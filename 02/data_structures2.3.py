# Data Structures Exercises 3
# By Gabriel Smith


def main():
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    slice1 = sampleList[0:3]
    slice2 = sampleList[3:6]
    slice3 = sampleList[6:9]
    sampleList.clear()
    sampleList.append(slice1)
    sampleList.append(slice2)
    sampleList.append(slice3)
    for i in range(0, 3, 1):
        sampleList[i].reverse()
    print(sampleList)


if __name__ == "__main__":
    main()
