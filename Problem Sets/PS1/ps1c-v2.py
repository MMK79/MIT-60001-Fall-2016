# Finding the right amount to save away
# Constant
total_cost = 1000000
semi_annual_rise = 0.07
current_saving = 0
r = 0.04

# User Entry
# annual_salary = 120000

# Test Case 1
# annual_salary = 150000

# Test Case 2
# annual_salary = 300000

# Test Case 3
annual_salary = 10000

#Bisection Search Variables
high = 10000
low = 0
# epsilon = 10000
guess_epsilon = 20
num_guess = 0
base_guess = (high + low)/2
last_guess = 0

#Target
portion_saved = base_guess/(10**4)

#Dependent Variables
portion_down_payment = 0.25*total_cost

while abs(last_guess - base_guess) >= guess_epsilon:
    month_count = 1
    portion_saved = base_guess/(10**4)
    monthly_salary = annual_salary/12
    monthly_save = portion_saved * monthly_salary
    for month_count in range(month_count,37):
        if month_count % 6 == 0:                
            monthly_salary += monthly_salary * semi_annual_rise
            monthly_save = portion_saved * monthly_salary
        current_saving += current_saving*r/12
        current_saving += monthly_save
        if month_count == 12:
            if current_saving > portion_down_payment/2:
                high = base_guess
        elif month_count == 18:
            if current_saving > portion_down_payment/2:
                high = base_guess
        if month_count == 36:
            if current_saving > portion_down_payment:
                high = base_guess
            elif current_saving < portion_down_payment:
                low = base_guess
    num_guess += 1
    current_saving = 0
    last_guess = base_guess
    base_guess = (high + low)/2
print (num_guess)
print (last_guess)