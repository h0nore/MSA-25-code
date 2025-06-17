"""
Function to get valid expression inputs from the user
Input: None
Outputs:(int)X, (int)X, (string) y
"""
def get_valid_expression_inputs():
    while True:
        expression = input("Expression: ").strip()
        parts = expression.split()
        if len(parts) != 3:
            print("Incorrect Format")
            continue

        try:
            x = int(parts[0])
            y = parts[1]
            z = int(parts[2])
            return x, y, z
        except ValueError:
            print("X and Z need to be integers")
            continue

"""
Functions to evaluate an expression
Inputs: X(int), Y (string), Z (int)
Output
"""
def evaluate_expression(x: int, y: str, z: int):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        try:
            return x / z
        except ZeroDivisionError:
            print("Error: division by 0 is not possible")
            return None
    else:
        print("ERROR: operators should be +, -, *, /")
        return None

def main():
    while True:
        # call the get_valid_expression_inputs function to get x, y, z
        x, y, z = get_valid_expression_inputs()
        
        # call evaluate_expression to get the answer for the expression
        result = evaluate_expression(x, y, z)
        
        # print the answer
        if result is not None:
            print("Result:", result)
        
        # ask the user if they want to continue
        cont = input("Do you want to continue? (y/n): ").strip().lower()
        if cont != 'y':
            break

main()
