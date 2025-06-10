#write a pounds to kilogram converter program
# A user will be prompted for their weight in pounds
# program will output weight in kgs

# GET INPUT WEIGHT FROM THE USER
#convert weight to a float
#validate that weight is a number
#if weight is not a number, remprompt the user until the input is correct
def get_postive_float_inpit():
    while True: 
        try:
            user_weight = float(input("Enter your weight in pounds/lbs: "))
            #validate that user_weight is postive. If not positive, reprompt the user.
            if user_weight <= 0: 
                print("Error: Enter a value greater than 0")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number")

    return user_weight

def main ():
   #get the weight from user, Call the get_positive_float_input
     user_weight = get_postive_float_inpit ()

    # PROCESSING
    # use a conversion to convert lbs to kilos : 2.205lbs = 1kg
    LBS_TO_KG_CONVERSION = 2.205
    user_weight_in_kg = user_weight / LBS_TO_KG_CONVERSION 

    #OUTPUT 
    #print the output to the user in a nice format to 2 decimal places
    print(f"you weight {user_weight_in_kg:.2f}kgs.")
    #call the main function

main()
