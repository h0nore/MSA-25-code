
def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students= ["Alice", "Bob]", "Jerry", "Jane", "Bill"]

    #print student name and score together
    for index in range (len(scores)):
        print(f"{students[index]}: {scores[index]}")

        #create a dicitonary of names and scores
    student_scores = {
        "Alice": 55,
        "Bob": 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91
    }

    #print Bob and Jane's scores
    print(student_scores["Bob"])
    print(student_scores["Alice"])

    #print all students data in the student scores dictionary
    print("\nGet all student data")
    for students in student_scores:
        print(f"{students}: {student_scores[students]}")

    #create a car dictionary to store make, model, year, engine type
    car_1 = {"make": "Ferrari", "Model": "F-50", "Year": 2021, "Value": 500000, "Engine": 4.8}
    #get all my car information
    print("\nGet the car information")

    for key, value in car_1.items():
        print (f"{key}: {value}")

    car_2 = {"make": "Honda", "Model": "Accord", "Year": 2015, "Value": 15000}

    #create a list of dictionaries
    dictionary_list = [car_1, car_2]

    print("\nDisplay all car information")
    for car in dictionary_list:
        print("\nCar Information")
        for feature, value in car.items():
            print(f"{feature}: {value}")
    #create a dictionary of dictionaries
    car_dictionary= {"Ferrai": car_1, "Honda": car_2}
    #Write a for loop to dispalay the car information
    #Ferrari
    #print all the info
    #Honda
    print("\nCar info from dictionary")
    for make in car_dictionary.items():
        print(make)
        for feature, value in car.items():
            print(f"{feature}: {value}")
main()