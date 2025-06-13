#the file demonstrates decision structers and conditions
def main():
    a = 7
    b = 14

    #exploring conditions
    print(f"A is greater than B: {a>b}")
    print(f"B is greater than A: {b>a}")
    print(f"A is equal to B: {a==b}")

    #comparison operators: 
    #less than: < , greater than >, less than or equal to <=, greater than or equal to >=
    # equal to ==

    #create a decision structure to determine if a and b are equal
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    #create a decision structure to print a letter garde based
    #on a test score
    #A: 100-90, B: 89 - 80, C: 79 - 70, D: 69 - 60, F less than 60
    print("Grade decision: 1")
    test_score = 75

           # A                       B
    if ((test_score <= 100) and (test_score >= 90)):
        print(f"{test_score}----> A")
    elif (test_score >=80):
        print (f"{test_score}---->B")
    elif (test_score >=70):
        print (f"{test_score}---->C")
    elif (test_score >=60):
        print (f"{test_score}---->D")
    elif (test_score >=0 ):
        print(f"{test_score}----> F")
    else:
        print(f"{test_score}----> Invalid test score!")

#create a decision structure to determine the seasons: Winter, Spring, Summer, Fall
#Ask user to enter the number of the month and based on the number, determine the season
#winter: 12, 1, 2; Spring: 3,4,5: Summer: 6,7,8: Fall: 9,10,11
#output/ print the season

   #get the weight from user, Call the get_positive_float_input
   
    start= int(input("Enter your month here: "))

    if((start >=9) and (start <=11)):
        print(f"{start}----Fall")
    elif ((start >=6) and (start<=8)):
        print (f"{start}----Summer")
    elif ((start >=3) and (start<=5)):
        print (f"{start}----Spring")
    elif (start == 1 or start==2 or start == 12):
        print (f"{start}----Winter")
    else:
        print (f"Invalid month number")




main()