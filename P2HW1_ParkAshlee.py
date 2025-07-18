# Ashlee Park
# 6/14/25
# P1HW2
# program for travel budget

print("This program calculates and displays travel expenses\n")
print("Enter Budget:", end=" ")
budget = int(input())
print("\n")

print("Enter your travel destination:", end=" ")
destination = input()
print("\n")

print("How much do you think you will spend on gas?", end=" ")
gas = int(input())
print("\n")

print("Approximately, how much do you think you will you need for accomodation/hotel?", end=" ")
hotel = int(input())
print("\n")

print("Last, how much do you need for food?", end=" ")
food = int(input())
print("\n")

print("---------Travel Expenses---------")
print("Location:", f"{destination:>10}")
print("Initial Budget:", f"${budget:.2f}")

print("Fuel:", f"        \t${gas:.2f}")
print("Accomodation:", f"\t${hotel:.2f}")
print("Food:", f"        \t${food:.2f}")
print("---------------------------------\n")
print("Remaining Balance:", f"${budget-gas-hotel-food:.2f}", end=" ")
    
