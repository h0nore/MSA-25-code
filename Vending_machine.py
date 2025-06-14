def main():
    
    #print vending machine
    print ("Vending Machine \n __________")

    amount_due = 50
    #use input function to get user input 
    #list accepeted values 1, 5, 10, 25
    accepted_coins = [ 1, 5, 10, 25]
    total_added = 0 
    #loop for adding money
    #validate input by using "if" statement 
    while total_added < amount_due:
        print (f"Amount due: {amount_due - total_added}")
        try:
            coin = int(input("insert coin here please:  "))
            if coin not in accepted_coins:
                print (f"Invalid coin, please insert either 1, 5, 10, or 25")
                continue
            total_added += coin
    #reprompt the user to add valid coins
        except: 
            print ("Please add a valid number for the coin")
            continue
        
    #subtract the valid coin to the total
    #calculate remaining balance with total due - amount paid
    change = total_added - amount_due

    #display amount due
    # if it is more than 50 cents, calculate the amount owed with total paid - target amount
    #display the amount owed back to user

    if total_added > amount_due:
        print (f"Change : {change}")

    print("Thank you have a good day :)")
        
    # if it is more than 50 cents, calculate the amount owed with total paid - target amount
    #display the amount owed back to user





main()