
class Student:
    def __init__(self,fn,ln,adharNo):
        self.firstName = fn 
        self.lastName = ln 
        self.adharNo = adharNo

    def displayName(self):
        print(self.firstName + self.lastName)

class Teacher(Student):
    def __init__(self,fn,ln,adharNo,salary):
        super().__init__(fn,ln,adharNo)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):
    def __init__(self, fn, ln, adharNo, salary,spec):
        super().__init__(fn, ln, adharNo, salary)
        self.special = spec

    def displaySpecialization(self):
        print(self.special)

bharat = Professor("bharat","bhate",213,4543534,"hindi")
print(bharat.firstName)
print(bharat.lastName)
print(bharat.adharNo)
print(bharat.salary)
print(bharat.special)

bharat.displayName()
bharat.displaySalary()
bharat.displaySpecialization()