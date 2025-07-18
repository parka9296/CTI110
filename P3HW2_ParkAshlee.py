#Ashlee Park
#P3HW2
#6/29/2025
#This program calculates an employees paycheck

print("Enter employee's name:", end=" ")
employee_name=input()
print("Number of hours worked:", end=" ")
hours=float(input())
print("Enter employee's pay rate:", end=" ")
rate=float(input())

print('-------------------------------------')
print("Employee Name:", employee_name, "\n")

reg_pay=hours*rate
gross=reg_pay
overtime=0
overtime_pay=0

if hours<=40:
 hours=reg_pay
elif hours>40:
 overtime=hours-40
elif overtime>0:
 overtime_pay=overtime*rate*1.5
 gross=overtime_pay+reg_pay
else:
 overtime=0

 
print("Hours Worked  Pay Rate   Overtime   Overtime Pay  RegHour Pay   Gross Pay")
print('-------------------------------------------------------------------------')
print(f"{hours}{rate:>15}{overtime:>10.2f}{overtime_pay:>12.2f}{reg_pay:>14.2f}${gross:>14.2f}$")
