#create a while loop thaty prints intengers between 0 and 10
output_value = 0
stop_value = 10

#run the loop while output value is less than or equal to stop_value
while output_value <= stop_value:
    print(output_value)
    #increment output_value by 1
    output_value= output_value + 1

print("\n\n")
output_value = 0
while True:
    print(output_value)
    #Increment output value by 1
    output_value += 1

    #if output_value is greater than stop value. Break the loop
    if output_value > stop_value:
        break
