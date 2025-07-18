#Ashlee Park
#P4HW2
#7/8/2025
#This program calculates an employees paycheck


print("Enter employee's name or 'Done' to terminate:", end=" ")
employee_name = input()

total_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0

while employee_name != "Done":
    print("How many hours did", employee_name, "work?", end=" ")
    hours = float(input())
    print("What is", employee_name,"'s pay rate?", end=" ")
    rate = float(input())

    print('-------------------------------------')
    print("Employee Name:", employee_name, "\n")

    overtime = 0
    overtime_pay = 0
    reg_pay = 0
    gross = 0

    if hours <= 40:
        reg_pay = hours * rate
        gross = reg_pay
    elif hours > 40:
        overtime = hours - 40
        reg_pay = 40 * rate
        overtime_pay = overtime * rate * 1.5
        gross = reg_pay + overtime_pay
    else:
        overtime = 0

    print("{:<13} {:<10} {:<10} {:<15} {:<15} {:<12}".format(
        "Hours Worked", "Pay Rate", "Overtime", "Overtime Pay", "RegHour Pay", "Gross Pay"))
    print('-------------------------------------------------------------------------')
    print("{:<13.2f} ${:<9.2f} {:<10.2f} ${:<14.2f} ${:<14.2f} ${:<11.2f}".format(
        hours, rate, overtime, overtime_pay, reg_pay, gross))
    print("\n")

    total_employees = total_employees + 1
    total_overtime_pay = total_overtime_pay + overtime_pay
    total_regular_pay = total_regular_pay + reg_pay
    total_gross_pay = total_gross_pay + gross

    print("Enter employee's name or 'Done' to terminate:", end=" ")
    employee_name = input()
    
else: 
    print("Total number of employees entered:", total_employees)
    print("Total amount paid for overtime: $", format(total_overtime_pay, ".2f"))
    print("Total amount paid for regular hours: $", format(total_regular_pay, ".2f"))
    print("Total amount paid in gross: $", format(total_gross_pay, ".2f"))
