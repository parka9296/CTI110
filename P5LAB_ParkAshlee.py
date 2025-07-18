#Ashlee Park
#7/12/25
#P5LAB
#program to simulate self checkout

import random

price=round(random.uniform(0.01, 100.00), 2)

print("You owe $", price)

print("How much cash will you put in the self-checkout?", end=" ")
cash=float(input())

change=cash-price
print("Change is:", f"{change:.2f}\n" )

  
cent=change
def disperse_change (change):

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

disperse_change(change)


