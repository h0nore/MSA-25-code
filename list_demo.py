#This file will demonstrate lists in python
def main():
    #we dont want to do this
    #name1 = "John"
    #name2 = "mary"

    #create list of names
    names = ["john", "Mary", "Alice", "Bob"]
    List_of_integers = [10, 16, 24, 43, 14, 19]
    random_datatype_list = {"cyd", 15, 22.3, "Frank"}

    print (names)

    #add an item to the names list
    names.append("Jane")
    List_of_integers.append(16)
    List_of_integers.append(14)
    
    print(names)
    print(List_of_integers)
    
    #get the numbers of items in a list
    print(f"\nNumber of items in the names list")
    number_of_items = len(names)
    print(f"Number of items in names list: {number_of_items}")

    #get the values from our list
    #get the first value from the list of integers
    print(f"\nFirst item in integer list: {List_of_integers[0]}")

    #get the fouth value from list of integer list
    print (f"\nFourth item in integer list; {List_of_integers[3]}")

    #print all item from the list of integers
    print("\n integer list items")
    for item in List_of_integers:
        print(item)

    print("\nIntegers list items using item indexes")
    #get the number of items in the integer list
    number_of_integer_items = len(List_of_integers)

    for index in range (number_of_integer_items):
        print(f"Item {index}: {List_of_integers[index]}")


        
main()