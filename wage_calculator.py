#Provide program that accepts input, performs a calculation, then displays the result as an output
#user is prompted for hours worked daily
#user is prompted for hourly wage
def get_positive_wage():
    while True:
        try:
            hourly_wage = float(input("Enter your hourly wage here: "))
            if hourly_wage <=0:
                print("Error, Please Enter a number greater than 0")
                continue
            else:
                break
        except:
            print("Please eneter just a number")
    return hourly_wage

#make sure not too little hours or too much
def get_hours_worked():
    while True:
        try:
            hours_worked = float(input("Enter your daily hours worked here: "))
            if hours_worked <= 0 or hours_worked > 24:
                print("Error, Please Enter a number greater than 0 or less then 24")
                continue
            else:
                break
        except:
            print("Please eneter just a number")
    return hours_worked

24
#calculate the yearly wage 
def calculate_yearly_wage(hourly_rate, hours_per_day):
    pretax= hourly_rate *hours_per_day *350
    taxed_wage = (hourly_rate * hours_per_day * 350) * 0.12
    yearly_wage = (hourly_rate* hours_per_day* 350)-taxed_wage
    return yearly_wage, pretax, taxed_wage
    
def main():
#get input of wage
    hourly_wage= get_positive_wage()
    hours_worked= get_hours_worked()
#do the calculation
    yearly_wage, pretax, taxed_wage = calculate_yearly_wage (hourly_wage, hours_worked)
    #do the output:
    print("Pay Advice")
    print("----------")
    print(f"Daily hours Worked: {hours_worked}")
    print(f"Hourly Wage: {hourly_wage}")
    print(f"wage before taxes: {pretax}")
    print(f"Tax amount: {taxed_wage}")
    print(f"Annual wage After Taxes: {yearly_wage}")
main()