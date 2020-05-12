# Control Flow Exercises 4
# By Gabriel Smith


class StudentRecord:
    def __init__(self, name, totalClasses, attendedClasses):
        self.name = name
        self.totalClasses = int(totalClasses)
        self.attendedClasses = int(attendedClasses)
        self.percentageClasses = "Not yet calculated, please run the calc func"
        self.finalEligible = "Not yet calculated, please run the calc func"

    def __str__(self):
        print(f'STUDENT NAME: {self.name}')
        print(f'TOTAL CLASSES: {self.totalClasses}')
        print(f'ATTENDED CLASSES: {self.attendedClasses}')
        print(f'ATTENDANCE PERCENTAGE: {self.percentageClasses}%')
        print(f'ELIGIBLE FOR FINAL: {self.finalEligible}')

    def calc(self):
        self.percentageClasses = int(round((
            self.attendedClasses / self.totalClasses) * 100))
        print(f'Attendance Percentage: {self.percentageClasses}%')
        if(self.percentageClasses >= 75):
            self.finalEligible = True
            return self.finalEligible
        else:
            self.finalEligible = False
            return self.finalEligible


def main():
    newRecord = StudentRecord(input("Please enter your name: "), input(
        "Please enter the total number of classes held: "), input("Please enter the classes in which you were present: "))
    # print(newRecord.__str__())
    if(newRecord.calc()):
        print(f'{newRecord.name}, you may take the final.')
    else:
        print(f'{newRecord.name}, you may not take the final.')
    # print(newRecord.__str__())


if __name__ == "__main__":
    main()
