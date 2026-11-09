





def factoraial(n):
    if (n==1 or n==0):
        return 1
    return n * factoraial(n-1)

n = int(input("enter a number:"))
print(f"The factoraial of this number is:{factoraial(n)}")