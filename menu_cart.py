"""
Function to load menu item and price into a dictionary
Input: (string)file_path
Output: (dictionary)menu 
"""
def get_menu_dictionary(file_name:str) -> dict:
    #open file.txt: create a file handler in read mode
    data_file = open("file.txt", "r")
    print(data_file)

    #create an empty dictionary to store item: price entries
    menu_items = {}

    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the data ant the comma
        item_name_and_price = line_of_data.strip().split(",")
        
        #skip lines that do not have both item and price
        if len(item_name_and_price) < 2:
            continue

        #get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price

    data_file.close()
    return menu_items
def display_cart(cart:dict, menu_items:dict)->None:
    print("\nCart\n---")
    total = 0 
    #loop through the car to print the output
    for item, quantity in cart.items():
        total = total + (quantity * menu_items[item])
        print(f"{quantity} {item} @{menu_items[item]:.2f}: {quantity * menu_items[item]:.2f}")
    print(f"\ntotal: {total:.2f}\n")
    return
"""
Function to write items from cart to receipt
Input(dict) cart
Output: None
"""


def print_receipt(cart: dict, menu_items: dict) -> None:
    with open("receipt.txt", "a") as receipt_file:
        total = 0
        receipt_file.write("Receipt\n-------\n")
        for item, quantity in cart.items():
            line_total = quantity * menu_items[item]
            total += line_total
            receipt_file.write(f"{quantity} {item} @{menu_items[item]:.2f}: {line_total:.2f}\n")
        receipt_file.write(f"\nTotal: {total:.2f}\n")
    print("Receipt written to receipt.txt")
          
def main():
    menu_item = get_menu_dictionary("file.txt")
    item_cart = {}
    while True:
        #prompt user for item
        item = input("\nItem: ")

        #determine if we need to end program
        if item.lower()== "end":
            #print the receipt with items from the cart
            print_receipt(item_cart,menu_item)
            break
     #validate that item is in the menu_item dictionary
        if item not in menu_item:
            print(f"\nERROR: {item} not on the menu")
            continue
        #prompt user for quantity
        try:
            quantity = int(input("Quantity:  "))
        except: 
            print("\nERROR: eneter a number for quantity")
            continue

        #add item to cart, if item in car already, quantinty
        #if not in cart, add item and quantity
        if item not in item_cart:
            #create a new entry in item_cart dictionary
            item_cart[item] = quantity
        else:
            #adds quantity to the value of the items current quantity
            item_cart [item] += quantity

            #display total by calling the display cards function
        display_cart(item_cart, menu_item)
            
main()