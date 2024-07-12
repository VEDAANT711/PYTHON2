# # duck typing 

class Duck:
    def talk(self):
        print('quack quack')

class Human:
    def talk(self):
        print('hello hi ')

def call_talk(obj):
    obj.talk()

d  = Duck()
# d.talk()

e = Human()
# e.talk()
call_talk(d)
call_talk(e)


# program 2
class Human:
    def talk(self):
        print("hello hi...")

class Duck:
    def talk(self):
        print("quack")

class Dog:
    def bark(self):
        print("Bow bow")

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()

a = Human()
b = Dog()
c = Duck()

call_talk(a)
call_talk(b)
call_talk(c)


# program 3  
# overloading --- same class , same methodName , different signature
# overriding  different class, same methodName , same signature

class Calculator:
    def addition(self, a= None,b=None,c=None,d = None):
        if(a != None and b != None and c != None and d != None):
            print(a+b+c+d)
        elif( a != None and b != None and c != None):
            print(a+b+c)
        elif(a != None and b != None):
            print(a+b)

a = Calculator()
a.addition(12,3,4,3)
a.addition(12,3,4)
a.addition(12,3)


class WorldBank:
    def save(self):
        print("I am saving method from worldBank")
    def loan(self):
        print("I am saving method from worldbank")

class SBI(WorldBank):
    def save(self):
        print("I am saving method from SBI")
    def loan(self):
        print("I am saving method from SBI")

class PNB(WorldBank):
    def save(self):
        print("I am saving method from PNB")
        super().loan()
    def loan(self):
        print("I am saving method from PNB")

d = SBI()
d.save()
d.loan()

d = PNB()
d.save()
d.loan()

