#This file will demonstrate how for loops work

def main():
    #print intengers between 0 and 10
    print("output numbers between 0 and 10")
    for number in range(11):
        print(number)

    #print integers between 5 and 10
    print("\n\noutput numbers between 5 and 10")
    for number in range(5,11):
        print(number)

    #print even numbers between 0 and ten
    print("\n\noutput even numbers between 0 and 10")
    for number in range (0, 11, 2):
        print(number)
  
    # print odd numbers between 0 and 10
    print("\n\noutput 0 numbers between 0 and 10")
    for number in range (1, 11, 2):
        print(number)

    #prompt a user for the start and stop values 
    # print the numbers between start and stop
    #get the start value from the user and convert to an intenger
    #get stop value from the user and convert to an intenger
    #create a loop to run from start to stop
    start= int(input("Enter your start value: "))
    stop = int(input("Enter your stop value:  "))
    print(f"n\n\noutput numbers from {start} to {stop}")
    for number in range (start, stop + 1):
        print (number)


    #use nested for loop to print multiplication tables from user input
    #user will provide start and stop
    start = int(input("Enter your start value: "))
    stop = int(input("Enter your stop value:  "))
    print(f"n\n\nPrint multiplication tables from {start} to {stop}")
    for table in range(start, stop + 1):
        print (f"\ndispalying the {table} multiplication table")
        for mutiple in range(1,13):
            product = table  * mutiple
            print(f"{table} x {mutiple} = {product}")
            


main()