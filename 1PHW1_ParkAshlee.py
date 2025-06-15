# Ashlee Park
# 6/14/25
# P1HW1
# program to do 2 math equations

print("-----Calculating Exponents-----\n")

print("Enter an integer as the base value:", end="  ")
base_value = int(input())
print("Enter an integer as the exponent:", end=" ")
exponent = int(input())
print("\n")

new_value = base_value ** exponent
print(base_value, "raised to the power of", exponent, "is", new_value, "!!")
print("\n")

print("-----Addition and Subtraction-----\n")

print("Enter a starting integer:", end=" ")
integer = int(input())
print("Enter an interger to add:", end=" ")
add = int(input())
print("Enter an integer to subtract:", end=" ")     
subtract = int(input())
print("\n")

print(integer, "+", add, "-", subtract, "is equal to", integer+add-subtract)      
