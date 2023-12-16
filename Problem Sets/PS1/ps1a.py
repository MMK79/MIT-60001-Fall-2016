# Part A:House Hunting
# total_cost = float(input('What is the total cost of your dream house?'))
# portion_saved = float(input('How much of percentage you can save?'))
# annual_salary = float(input('What is your annual Salary'))

# Test Case 1
total_cost = 1000000
portion_saved = 0.10
annual_salary = 120000

# total_cost = 500000
# portion_saved = 0.15
# annual_salary = 80000

month_count = 0
current_saving = 0
r = 0.04

portion_down_payment = 0.25*total_cost
print(portion_down_payment)

monthly_salary = annual_salary/12
print(monthly_salary)

monthly_save = portion_saved*monthly_salary
print(portion_saved)

while current_saving <= portion_down_payment:
    current_saving += current_saving*r/12
    current_saving += monthly_save
    if month_count == 182:
        print(current_saving)
    month_count += 1
print(month_count)
