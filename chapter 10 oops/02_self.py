class Employee:
    language = "python"  #this is an class attributes
    salary = 120000

def getInfo(self):
 print(f"the language is {self.language}.the salary is {self.salary}")
 def greet(self):
    print("good morning")

dev = Employee()
# dev.language = "javascript" #and this is an object attributes
print( dev.language, dev.salary)
dev.getInfo()
dev.greet()
# Employee.getInfo(dev)

