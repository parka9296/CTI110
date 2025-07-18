#Ashlee Park
#7/8/45
#P4HW1_ParkAshlee
#program to display a letter grade for the calculated average

score_list=[]

print("How many scores do you want to enter?", end=" ")
grade=int(input())

print("\n")

for grade in range(1,grade+1):
    print("Enter score #",grade, ":", end=" ")
    score=int(input())
    
    if score<0 or score>100:
        print("INVALID score entered!!!")
        print("Score should be between 0 and 100")
        print("Enter score #", grade, "again:", end=" ")
        score=int(input())

    score_list.append(score)
    
print("\n")

print("-------Results-------")


#print(score_list)
    
lowest=min(score_list)

score_list.remove(min(score_list))
#print(score_list)

average=sum(score_list)/len(score_list)


print("Lowest score:", lowest)
print("Modified list:", score_list)
print("Scores Average:", average)

if average>=90:
     print("Grade: A")
elif 80<=average<90:
     print("Grade: B")
elif 70<=average<80:
     print("Grade: C")
elif 60<=average<70:
     print("Grade: D")
else:
     print("Grade: F")
     
print("--------------------")
