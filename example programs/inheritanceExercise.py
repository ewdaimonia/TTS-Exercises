# You are given two classes, Person and Student, where Person is the base class and Student is the derived class.
# Completed code for Person and a declaration for Student are provided for you in the editor.
# Observe that Student inherits all the properties of Person.

# Complete the Student class by writing the following:
# A Student class constructor, which has 4 parameters:
# - A string, firstName
# - A string, lastName
# - An integer, id
# An integer array (or vector) of test scores, scores

# A char calculate() method that calculates a Student object's average and returns the grade character
# representative of their calculated average:
# A | 90-100
# B | 80-89
# C | 70-79
# D | 60-69
# F | <60

class Person(object):
    def __init__(self, firstName="Bob", lastName="Jones"):
        self.firstName = firstName
        self.lastName = lastName


class Student(Person):
    def __init__(self, firstName="Bob", lastName="Jones", id=700, scores=[0, 0]):
        self.id = id
        self.scores = scores
        super().__init__(firstName, lastName)

    # def __init__(self, person, id, scores):
    #     self.id = id
    #     self.scores = scores
    #     self.firstName = person.firstName
    #     self.lastName = person.lastName

    def calculate(self):
        self.scores = list(map(int, self.scores))
        if(sum(self.scores) < 60):
            return "F"
        elif(70 > (sum(self.scores)/len(self.scores)) >= 60):
            return "D"
        elif(80 > (sum(self.scores)/len(self.scores)) >= 70):
            return "C"
        elif(90 > (sum(self.scores)/len(self.scores)) >= 80):
            return "B"
        elif(100 >= (sum(self.scores)/len(self.scores)) >= 90):
            return "A"
        else:
            return "+++A"

    def __str__(self):
        return (self.firstName + " " + self.lastName + " " + str(self.id) + " " + str(self.scores))


def main():
    # newPerson = Person("Guy", "Francis")
    # personToStudent = Student(newPerson, 8, [
    #     "4", "62", "300", "45", "92"])
    # print(personToStudent)

    newStudent = Student("Craig", "Hightower", 45, [
                         "4", "62", "300", "45", "92"])
    listOfStudents = [newStudent]
    print(str(newStudent), newStudent.calculate())
    cont = "y"
    while(cont == "y"):
        listOfStudents.append(Student(input("First name:"), input("Last name:"), input(
            "ID:"), input("Scores(ENTER AS A SPACE SEPARATED LIST):").split()))
        cont = input("Add another student?(y/n)")
    for i in listOfStudents:
        print(str(i) + " " + i.calculate())


if __name__ == "__main__":
    main()
