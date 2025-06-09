# Print hello world
print("hello world!")

#create a variable to store my name
first_name= "Honore"

#print "My name is Honore
print("My name is", first_name)
 
#create a variable to store my last name
last_name= "Irumva"

#write a statement to display "My full name is fistname lastname"
print("My full name is", first_name, last_name,sep="---")

# variables to store your age, height, weight, and assign them values
age= 16
height = 74
weight= 145.5

#print a sentence with age, weight, height
print(f"my name is{first_name} {last_name}\nI am {age} years old and I weigh {weight} lbs")

#get and print the data type for age, weight, and height
print(type(age))
print(type(weight))
print(type(height))

#write 3 print statements using string interpolation (fstring) to print 
#descriptive sentences for the data types
age="int"
weight="float"
height="int"
print(f"variable age is an {age}, variable weight is a {weight}, and variable height is an {height}")

number_1 = 5
number_2 = 7
total = number_1 + number_2
print(f"total: {total}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"total: {total}")