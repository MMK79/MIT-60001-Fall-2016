# Part A:House Hunting
# total_cost = float(input('What is the total cost of your dream house?'))
# portion_saved = float(input('How much of percentage you can save?'))
# annual_salary = float(input('What is your annual Salary?'))
# semi_annual_rise = float(input('What is the percentage of your rasie?'))

# # Test Case 1
# total_cost = 500000
# portion_saved = 0.05
# annual_salary = 120000
# semi_annual_rise = 0.03

# Test Case 2
# total_cost = 800000
# portion_saved = 0.1
# annual_salary = 80000
# semi_annual_rise = 0.03

# Test Case 3
# total_cost = 1500000
# portion_saved = 0.05
# annual_salary = 75000
# semi_annual_rise = 0.05

# Test Case 3
total_cost = 1000000
portion_saved = 0.5
annual_salary = 120000
semi_annual_rise = 0.07

month_count = 0
current_saving = 0
r = 0.04

portion_down_payment = 0.25*total_cost
monthly_salary = annual_salary/12
monthly_save = portion_saved*monthly_salary

while current_saving <= portion_down_payment:
    if month_count % 6 == 0 and month_count != 0:
        monthly_salary += monthly_salary * semi_annual_rise
        monthly_save = monthly_salary * portion_saved
    current_saving += current_saving*r/12
    current_saving += monthly_save
    month_count += 1
    if month_count == 36:
        print(current_saving)
print(month_count)

