from Student import Student
from datetime import datetime
"""
Function to write an error message to a log file
Input: (string) error message
Output none
"""
def write_to_error_log(message:str) -> None:
    #open the log file in append mode: error log.txt
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()}: {message}\n")
   

    #write error message to the file  in the format

    #Date: message >5/24/2025: Error in data file on line 5

    #close file 

    return
"""
Function to return a list of student obejcts
input :none
Output:list of students

"""

def load_students():
    student_file = open("students.csv", "r")
    
    line_number= 0
    student_list = []
    
    for line in student_file:
        line_number +=1
        if line_number == 1:
            continue
        line_of_data = line.split(",")

        if len(line_of_data) != 6:
            message = f"Error: Incorrect data format on line {line_number}"
            write_to_error_log(message)
            continue   

        try:
            the_student = Student(line_of_data [0], line_of_data [1], line_of_data [2], int(line_of_data[3]), float(line_of_data[4]), line_of_data [5])
            student_list.append(the_student)
    
        except:
            message = f"Error: Credit hours and/or gpa a number on {line_number}"
            write_to_error_log(message)
            continue
    student_file.close()
    
    print("\nStudent Data:\n")
    for student in student_list:
        student.print_student_data()
    return student_list

"""
Function to convert student object to student dicitionaries
Input: list of student objects
Output: List of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create a list to store a dictionary in
    student_dictionary_list = []

    #loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dicitonary
        student_dictionary = {}
        #set the keys and values for the dictionary
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id_number()

        #append the dictionary to the list of dictionaries 
        student_dictionary_list.append(student_dictionary)
    #return the list of dictionary
    return student_dictionary_list

"""
Function to get a list of student dicitionaries
Input: none
Output: List of student dictionaries
"""
def get_student_dictionaries():
    #get a list of students
    students_list = load_students()

    #get a list of student dictionaries
    student_dictionaries = student_to_dictionary(students_list)

        
    return student_dictionaries

