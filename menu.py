"""
Function to load menu item and price into a dictionary
Input: (string) file_path
Output: (dictionary)
"""
def get_menu_dictionary(file_name: str) -> dict:
    menu = {}
    try:
        # Open file in read mode
        with open(file_name, "r") as file:
            for line in file:
                # split code by comma for item and price
                parts = line.strip().split(",")
                if len(parts) != 2:
                    continue  # skip lines that don't have exactly 2 values
                item, price = parts
                menu[item] = float(price)
                
    except FileNotFoundError:
        print(f"Error, file not found")
    return menu
  
def main():
    # load menu items from file
    menu_item = get_menu_dictionary("file.txt")
    total_cost = 0
    while True:
        # prompt the user to enter a menu item
        item = input("Enter a menu item or 'end' to finish:  ").strip().title()
        # check if user wants to end program
        if item.lower() == "end":
            break
        # check if item is on the menu
        elif item in menu_item:
            total_cost += menu_item[item]
            # display total to 2 decimal places
            print(f"Total cost: ${total_cost:.2f}")
        # tell them if item isn't found
        else:
            print("Item not found, please enter a valid menu item")
    # print the final cost after loop ends
    print(f"Final cost: ${total_cost:.2f}")
    

main()