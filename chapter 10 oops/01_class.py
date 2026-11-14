class Employee:
    language = "python"  #this is an class attributes
    salary = 120000

dev = Employee()
dev.language = "javascript" #and this is an object attributes
print( dev.language, dev.salary)

rohan = Employee()
rohan.name = "rohan rohan "
print( rohan.name,rohan.language, rohan.salary)


#  here name is object attributes and the salary  and language  are class attributes as they directly belong to the class