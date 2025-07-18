#Ashlee Park
#7/7/25
#P4LAB2
#program that asks user to enter an integer and displays a multiplication table


print("Enter an integer:", end=" ")
integer = int(input())

for i in (1,2,3,4,5,6,7,8,9,10,11,12):
  result = integer*i
  if integer<0:
      break
  print(integer, "*", i, "=", result)

if integer<0:
 print("This program can't handle negative numbers")
 print("Would you like to run this program again?", end=" ")
 user_response=input()

 
if integer>=0:
 print("Would you like to run this program again?", end=" ")
 user_response=input()

 
while user_response=="yes":
    print("Enter an integer:", end=" ")
    integer = int(input())
    
    if integer<0:
     print("This program can't handle negative numbers")
    else:
     for i in (1,2,3,4,5,6,7,8,9,10,11,12):
      result = integer*i
      if integer<0:
        break
      print(integer, "*", i, "=", result)
      
    print("Would you like to run this program again?", end=" ")
    user_response=input()

else:
    user_response=="no"
print("Exiting program...")


  


 


    

  

