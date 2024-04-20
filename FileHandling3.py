import pickle
class Emp:
    def __init__(self,fn,ln,salary):
        self.firstname = fn
        self.lastname = ln
        self.slary = salary
    

    def UserInfo(self):
        print(self.firstname)
        print(self.lastname)
        print(self.salary)

f = open('emp.dat',"wb")
user = int(input("ENTER THE NUMBER OF USER'S ="))


for x in range(user):
    fn = input("Enter Firstname =")
    ln= input("Enter the Lastname =")
    salary= input("enter the Salary =")

    e = Emp(fn,ln,salary)
    pickle.dump(e,f)


f.close()   
f= open('emp.dat',"rb")
while True:
    try:
       e = pickle.load(f)
       e.UseInfo()
    except:
        print("EOF Reached")
        break
f.close()
















