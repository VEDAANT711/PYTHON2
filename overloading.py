
class Calculator:
    def addition(self,x,y):
        print(x+y)

    def addition(self,x,y,z):
        print(x+y+z)

    def addition(self,x,y,z,a):
        print(x+y+z+a)

    def addition(self , x = None , y = None , z = None , a = None):
        if(x != None and y != None  and z != None  and a != None):
            print(x+y+z+a)
        elif(x != None and y != None and z != None):
            print(x+y+z)
        elif(x != None and y != None):
            print(x+y)

cal = Calculator()
cal.addition(23,4)
cal.addition(23,4,5)
cal.addition(23,41,50,50)



class Dog:
    def talk (self):
        print("Bhow-Bhow")

class Cat:
    def talk (self):
        print("Meow-Meow")

class Cow:
    def sound(self):
        print("Mowh-Mowh")   

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()
        
        
a = Dog()
b = Cat()
c = Cow()

call_talk(a)
call_talk(b)
call_talk(c)
