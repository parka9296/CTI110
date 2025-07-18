#Ashlee Park
#6/29/2025
#PLAB3
#This program takes a number grade, determines average and displays letter grade for average.


# Enter grades for six modules

print('Enter grade for Module 1:', end=" ")
mod_1 = float(input())
print('Enter grade for Module 2:', end=" ")
mod_2 = float(input())
print('Enter grade for Module 3:', end=" ")
mod_3 = float(input())
print('Enter grade for Module 4:', end=" ")
mod_4 = float(input())
print('Enter grade for Module 5:', end=" ")
mod_5 = float(input())
print('Enter grade for Module 6:', end=" ")
mod_6 = float(input())

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# TO DO: determine lowest, highest , sum and average for grades
print('--------Results---------')
print(f'Lowest Grade:\t{min(grades):.2f}')
print(f'Highest Grade:\t{max(grades):.2f}')
print(f'Sum of Grades:\t{sum(grades):.2f}')
print(f'Average:\t{sum(grades)/len(grades):.2f}')
print('------------------------')

# determine letter grade for average
average=sum(grades)/len(grades)
if average >= 90:
    print('Your grade is: A')
elif average >=80:
    print('Your grade is: B')
elif average >=70:
    print('Your grade is: C')
elif average >=60:
    print('Your grade is: D')
else:
    print('Your grade is: F') # TO DO: finish this

