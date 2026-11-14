class Employee:
    language ="python"
    salary =120000

    def __init__(self,name,salary,language):# dunder method  is automatically called when we create and object of a class
        self.name = name
        self.salary = salary
        self.language = language
        print(" I am creating an object ")
 
def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("good morning")

    
        dev = Employee("dev",120000,"python")
        # dev.name ="dev"
        print(dev.name,dev.salary)