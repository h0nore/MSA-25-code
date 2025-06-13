#function: get the name of the season
#Input : number of the month
#Output: (string) name of month
def get_season_name(start):
 
    if((start >=9) and (start <=11)):
        return "Fall"
    elif ((start >=6) and (start<=8)):
        return "summer"
    elif ((start >=3) and (start<=5)):
        return "spring"
    elif (start == 1 or start==2 or start == 12):
        return "winter"
    return start
#function:
#Input
#Output: (int) name of month
def get_month_number():
    #validate the input is 1-12
    #reprompt user if input is not valid
    while True: 
        try:
            month_number = int(input("Enter the month here: "))
            
            if month_number <= 0: 
                print("Error: Enter a value greater than 0")
                continue
            elif month_number >12:
                 print("Please enter a number under 12")
                 continue
            else:
                break
        except:
            print("Enter a valid number")

    
    return month_number

def retry():
    print ("Would you like to restart the program?")
    answer= input(" Enter Y or y for yes or anything else for no:  ")
    if ((answer== "Y") or (answer =="y")):
        rerun = True
    else:
        rerun= False
    return rerun
def main():
    while True:
    #call the get_month_number function to prompt and get the month number from the user
     month_number = get_month_number()

    #call the get_season_name function to get the name of the season
     season= get_season_name(month_number)

    #print the output
     print (f"It is {season}")

    #ask the user if they want to run the program again
     rerun= retry()
     if rerun == True:
        continue
     else:
        break



main()