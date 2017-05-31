students = []

def get_students_titlecase():
    students_titlecase = []
    for student in students:
        students_titlecase.append(student["first_name"].title())
    return students_titlecase

def print_students_titlecase():
    students_titlecase = get_students_titlecase()
    print(students_titlecase)

def add_student(first_name, last_name, student_id):
    student = {"first_name": first_name, "last_name": last_name, "Student_id": student_id }
    students.append(student)

def save_file(first_name, last_name, student_id):
    try:
        f = open("betterstudents.txt", "a")
        f.write(first_name + " " + last_name + " " + student_id + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("betterstudents.txt", "r")
        for student in f.readlines():
            add_student(student)
        f.close()
    except Exception:
        print("Could not read file")





def main():

    while True:
        option = input("Would you like to enter and additional student (y/n)")
        if option == "y":

            read_file()

            student_first_name = input("Enter student first name: ")
            student_last_name = input ("Enter student last name: ")
            student_id = int(input("Enter student ID: "))

            add_student(student_first_name, student_last_name, student_id)
            save_file(student_first_name, student_last_name, student_id)
        elif option == "n":
            read_file()
            print_students_titlecase()
            print("\n""\n" + "Goodbye")
            break
        else:
            print("Please enter a valid option. ")
main()




