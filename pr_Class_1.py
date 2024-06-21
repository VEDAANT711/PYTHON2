class Person:
    fn = "vedant"
    ln = "gaikwad"
    def display(self):

         print(self.fn+self.ln) 

vedant = Person()
vedant.display()  

vedu = Person()
vedu.display()

vedu.fn = "vedu"
vedu.ln = "007"

vedu.display()

class Hello:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def display(self):
        print(self.firstname+self.lastname)

v = Hello("vedu","hello")
v.display()


class Person:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName =  ln 

    def display(self):
        print(self.firstName + self.lastName)

ninad = Person("ninad","dani") 
ninad.display()     
           
