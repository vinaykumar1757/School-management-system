class Student:
    student_dictionary = {}
    school_name = "Delhi Public School"

    def __init__(self):
        self.roll_no = input("Enter the Student Roll Number: ")
        self.name = input("Enter the Student Name: ")
        self.phone_number = input("Enter Phone Number: ")
        student_class = input("Enter the Student class: ")

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)
            StudentClass.classes[student_class] = new_class

        self.student_class = StudentClass.classes[student_class]

        print("Student Added Successfully")
        self.getStudent()

    def getStudent(self):
        print()
        print("--STUDENT DETAILS--")
        print("Roll Number:", self.roll_no)
        print("Name:", self.name)
        print("Phone Number:", self.phone_number)
        print("School Name:", Student.school_name)

    def updateStudent(self):
        print("Select option to update student details:")
        print("1) To change student name")
        print("2) To change student phone number")
        print("3) To change student class")
        print()

        option = input("Enter any of the above options: ")
        print()
        if option in ["1", "2", "3"]:
            if option == "1":
                self.name = input("Enter the Student New Name: ")
                print("Student Name Changed Successfully")
            elif option == "2":
                self.phone_number = input("Enter the Student New Phone Number: ")
                print("Student Phone Number Changed Successfully")
            elif option == "3":
                new_class = input("Enter the Student New Class Name: ")
                self.student_class.studentList.remove(self)
                if new_class in StudentClass.classes:
                    self.student_class = StudentClass.classes[new_class]
                else:
                    addClass = StudentClass(new_class)
                    StudentClass.classes[new_class] = addClass
                    self.student_class = addClass
                self.student_class.studentList.append(self)
                print("Student Class Changed Successfully")
        else:
            print("You have chosen the wrong option")

    @classmethod
    def updateSchoolName(cls, new_school_name):
        cls.school_name = new_school_name

    @classmethod
    def getTotalStudentCount(cls):
        return len(cls.student_dictionary)


class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        self.studentList = []
        StudentClass.classes[name] = self


def main():
    print(f"--Welcome to {Student.school_name}--")
    print("1) To Get Student Details")
    print("2) To Add New Student")
    print("3) To Remove Student")
    print("4) To Update Student Details")
    print("5) To Update School Branch")
    print("6) To Get Number of Students in School")
    print("7) To Get All Students' Details")
    print("8) To Get Any Class Student Details")
    print()

    option = int(input("Enter Any Above Given Option: "))

    if option == 1:
        roll_no = input("Enter the Roll Number of a Student: ")
        if roll_no in Student.student_dictionary:
            Student.student_dictionary[roll_no].getStudent()
            print()
        else:
            print("You have entered the wrong roll number")
            print()

    elif option == 2:
        new_student = Student()
        Student.student_dictionary[new_student.roll_no] = new_student
        print()

    elif option == 3:
        roll_no = input("Enter the Roll Number of a Student: ")
        if roll_no in Student.student_dictionary:
            student = Student.student_dictionary.pop(roll_no)
            student.student_class.studentList.remove(student)
            print(f"Student with roll number {roll_no} deleted successfully")
            print()
        else:
            print("No student found with that roll number")
            print()

    elif option == 4:
        roll_no = input("Enter the Roll Number of a Student: ")
        print()
        if roll_no in Student.student_dictionary:
            Student.student_dictionary[roll_no].updateStudent()
        else:
            print("You have entered the wrong roll number")

    elif option == 5:
        new_school_name = input("Enter the new School Name: ")
        Student.updateSchoolName(new_school_name)
        print("School Name Changed Successfully")

    elif option == 6:
        print("Total Number of Students in School:", Student.getTotalStudentCount())
        print()

    elif option == 7:
        if Student.student_dictionary:
            print("Total Number of Students in School:", Student.getTotalStudentCount())
            print("Total Student List with Details:")
            print()
            for sNo, student in enumerate(Student.student_dictionary.values(), start=1):
                print(f"Student {sNo}:")
                student.getStudent()
                print()
        else:
            print("No students found")
            print()

    elif option == 8:
        class_name = input("Enter the Class Name: ")
        if class_name in StudentClass.classes:
            student_class = StudentClass.classes[class_name]
            print(f"Students of class {student_class.name}")
            print(f"Total Number Of Students in Class {student_class.name}: {len(student_class.studentList)}")
            print()
            for sNo, student in enumerate(student_class.studentList, start=1):
                print(f"Student {sNo}:")
                student.getStudent()
                print()
        else:
            print("You entered the wrong class name or no students found")
            print()


if __name__ == "__main__":
    option = "yes"
    while option.lower() == "yes":
        main()
        option = input("Do you want to continue? [yes/no]: ")
        print()
