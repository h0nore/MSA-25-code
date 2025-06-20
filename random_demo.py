import random

#Promt the user for dificulty (1,2,3), and validate the inputs

def get_difficulty_level():
    while True:
        try:
            level = int(input("Enter difficulty level (1, 2, or 3): "))
            if level in [1, 2, 3]:
                return level
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
# get the number of questions & validate the input 
def get_number_of_question():
     while True:
        try:
            number_of_questions = int(input("Enter the amount of questions you would like (3-10): "))
            if 3<= number_of_questions <=10:
               return number_of_questions
    #wrong amount of questions selected
            else:
               print(f"Invalid numbers, please enter numbers 3-10.")
    #if input isn't a number
        except ValueError:
            print("Invalid input. Please input a number")
#generate an addition problem based on the level selected\
def addition_problem(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y 

def main():
    #return everything and create the adding system
    level= get_difficulty_level()
    numer_of_questions = get_number_of_question()

    correct_answers = 0
    for i in range(numer_of_questions):
        x, y = addition_problem(level)
        right_answer = (x + y)
        amount_of_tries = 0
        while amount_of_tries < 3:
            try:
                user_answer = int(input(f"Problem {i + 1}: {x} + {y} =  "))
                if user_answer == right_answer:
                    print("Correct!!!!")
                    correct_answers +=1
                    break
                else:
                    print("Wrong answer :( please try again)")
    #add to the amount tried after getting it wrong
                    amount_of_tries +=1
            except ValueError:
                print("Invalid input. Please input a valid number" )
                amount_of_tries +=1
    #say the correct answer after the max tries have been reached
        if amount_of_tries == 3:
            print(f"The correct answer was {right_answer}")

    score = correct_answers
    percentage = (correct_answers / numer_of_questions) * 100

    print("\n ---Game Over---\n")
    #print score
    print(f"Your score is: {score} / {numer_of_questions}")
    #percentage
    print(f"Percentage Correct: {percentage:.2f}%")

main()