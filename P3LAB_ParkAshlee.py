#Ashlee Park
#6/30/25
#P3LAB
#program that breaks down a money amount into change



print('Enter the amount of money as a float: $', end=" ")
cent=float(input())

total_cents=round(cent*100)

dollars=total_cents//100
total_cents=total_cents-(dollars*100)

quarters=total_cents//25
total_cents=total_cents-(quarters*25)

dimes=total_cents//10
total_cents=total_cents-(dimes*10)

nickels=total_cents//5
total_cents=total_cents-(nickels*5)

pennies=total_cents//1
total_cents=total_cents-(pennies*1)

if dollars>0:
    if dollars==1:
        print("1 Dollar")
    else:
            print(dollars, "Dollars")

if quarters>0:
    if quarters==1:
        print("1 Quarter")
    else:
            print(quarters, "Quarters")

if dimes>0:
    if dimes==1:
        print("1 Dime")
    else:
            print(dimes, "Dimes")
            
if nickels>0:
    if nickels==1:
        print("1 Nickel")
    else:
            print(nickels, "Nickels")
            
if pennies>0:
    if pennies==1:
        print("1 Penny")
    else:
            print(pennies, "Pennies")

if dollars==quarters==dimes==nickels==pennies==0:
    print("No change")

