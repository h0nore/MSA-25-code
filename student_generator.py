from Student import Student
def main():
    student_file = open("students.csv", "r")

    student_list = []
    
    for line in student_file:
        line_of_data = line.split(",")

        if len(line_of_data) != 6:
            continue   

        try:
            the_student = Student(line_of_data [0], line_of_data [1], line_of_data [2], int(line_of_data[3]), float(line_of_data[4]), line_of_data [5])
            student_list.append(the_student)
    
        except:
            continue
    student_file.close()
    
    print("\nStudent Data:\n")
    for student in student_list:
        student.print_student_data()


main()

