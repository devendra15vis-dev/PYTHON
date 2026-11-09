a=int(input("enter your age:")) 
# if statement no 1 

if(a%2==0):
    print("a is even")

#  End of if statement no 2
if(a>=18):
    print("you are above the age of consent")
    print("Good for you")

elif(a<0):
    print("you are not above the age of consent")
elif(a==0):
    print("you are entering 0 which is not a valid age")

else:
    print("you are below the age of consent")
    # End of if statement no 2


    print("End of program")