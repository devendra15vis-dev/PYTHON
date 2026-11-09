marks1=int(input("enter marks1:"))
marks2=int(input("enter marks2:"))
marks3=int(input("enter marks3:"))

#check for total percentage
total_percentage= (100 * (marks1 + marks2 + marks3))/300

if (total_percentage >=40):
    print("you are pass")

 else:
    print("you are fail")