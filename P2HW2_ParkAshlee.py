#Ashlee Park
#6/24/2025
#P2HW2
#program to display grades

Grades=[65.5, 88, 78.5, 90, 61, 92]

print(f"Enter grade for Module 1: {Grades[0]}")
print(f"Enter grade for Module 2: {Grades[1]}")
print(f"Enter grade for Module 3: {Grades[2]}")
print(f"Enter grade for Module 4: {Grades[3]}")
print(f"Enter grade for Module 5: {Grades[4]}")
print(f"Enter grade for Module 6: {Grades[5]}\n")

print("------Results------")
print("Lowest Grade:\t", min(Grades))
print("Highest Grade:\t", max(Grades))
print("Sum of Grades:\t", sum(Grades))
print(f"Average:\t{sum(Grades)/len(Grades):.2f}")
print("-------------------")
                  
