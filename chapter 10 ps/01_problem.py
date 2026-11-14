class programmer:
    company = "microsoft"
    def __init__(self, name, salary, pin_code):
        self.name = name
        self.salary = salary
        self.pin_code = pin_code


        p = programmer("dev",120000,274202)
        print(p.name,p.salary,p.pin_code,p.company)
