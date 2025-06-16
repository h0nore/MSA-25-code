
def main():
    my_name = "honore"
    #capitalize a string
    print(my_name.capitalize())


#make a string uppercase
    print(my_name.upper())
    
    #make a string lowercase
    last_name = "IRUMVA"
    print (f"{my_name.lower()} {last_name.lower()}")

    print("\nUsing startswith () method")
    #determine if a string starts with a set of charcters
    print(my_name.startswith("h") or my_name.startswith("H"))

    if (not my_name.startswith("hon") and not my_name.startswith ("Hon")):
        print(f" You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly.")
    
    print(f"Using endswith() method")
    print(f"{my_name} ends with 'ore': {my_name.endswith("ore")}")

    print("\nUsing the find() method")
    #find the o in Honore
    search_letter = "x"
    print(f"The 'x' is at index {my_name.find("x")} in {my_name}")

    if (my_name.find ("x") == -1):
        print(f"there is no {search_letter} in {my_name}")
    else:
        print(f"The {search_letter} is at index {my_name.find(search_letter)} in {my_name}")   
        
    #Loop through a string
    print("\nLoop through a string")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")

    #print the letters in a string along with the index postion
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index}: {my_name[letter_index]}")

    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of occurances of the word dog in the sentence
    #expected output : 3
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    #use a while loop
    while True:
        #start a the beginning of the string
        #search for the first occurance of the word (dog) starting from index 0
        dog_index = sentence.find(search_word, start_index )

        #if we find a dog, add 1 to some variable of dogs we found
        #update the start index to dog index +1
        if dog_index == -1:
            break
        else:
            number_of_dogs +=1
        #coninue searching the string for the next index afer the dog we found
            start_index = dog_index + 1
        #do this until we don't find any more dogs
    print(f"There are {number_of_dogs} {search_word} in the sentence")
    
    #how to use the split method
    print("\nUsing the split () method")
    car_info = "Ferrari,f-50,2021,500000,4.8\n"
    car_data = car_info.split(",")
    print(car_data)
    #get individual pieces of data
    make = car_data[0]
    model= car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"price: ${price} - Engine: {engine_size}L")



main()

  