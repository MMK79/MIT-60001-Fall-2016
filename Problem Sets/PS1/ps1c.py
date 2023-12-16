# Finding the right amount to save away
# Constant
total_cost = 1000000
semi_annual_rise = 0.07
current_saving = 0
r = 0.04

# User Entry
# annual_salary = 120000

# Test Case 1
annual_salary = 150000

# Test Case 2
# annual_salary = 300000

# Test Case 3
# annual_salary = 10000

#Bisection Search Variables
high = 10000
low = 0
epsilon = 100
num_guess = 0
guess = (high + low)/2

#Target
portion_saved = guess/(10**4)

#Dependent Variables
portion_down_payment = 0.25*total_cost
monthly_salary = annual_salary/12
monthly_save = portion_saved*monthly_salary

while abs(current_saving - portion_down_payment) >= epsilon:
    monthly_salary = annual_salary/12
    monthly_save = portion_saved * monthly_salary
    current_saving = 0
    month_count = 1
    for month_count in range(month_count,37):
        if monthly_salary % 6 == 0:
            monthly_salary += monthly_salary*semi_annual_rise
            monthly_save =  monthly_salary*portion_saved
        current_saving += current_saving*r/12
        current_saving += monthly_save
    
    if current_saving < portion_down_payment:
        low = guess
    else:
        high = guess
    
    num_guess += 1
    guess = (high + low)/2
    portion_saved = guess/(10**4)
print(num_guess)
print(portion_saved)