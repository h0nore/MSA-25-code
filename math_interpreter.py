def main():
    #Prompt the user to enter a math expression in the format X y Z where y is a math operator
    while True:
        expression = input("Expression: ").strip()
    #split the inputs to get the parts of the expression
        parts = expression.split()
    #check the length of the list returned from .split
    #if len(list) not = 3, output incorrect format message and rempromt
        if len(parts)!= 3:
            print("Incorrect Format")
            continue

    #get X Y and Z values from the list
    try:
        x= int(parts[0])
        y = parts[1]
        z= 
        
    #and check if they are integers by converting to int()
    #except:
    #   output Error message and rempromt
    
    #check that operator is +, -,*, /
    #if operator not in [+,-,*,/]
    #output some error message
    # rempromt the user

    #determine the operation to carry out the expression

main()