class Person:
    first_name =  "vedant"
    last_name  = "gaikwad"
    def walk(self):
        print("i am walking")

    def talk(self):
        print("i am talking")
        
vedant = Person()
print(vedant.first_name)
print(vedant.last_name)
vedant.talk()
vedant.walk()

siddhu = Person()
print(siddhu.first_name)
print(siddhu.last_name)
siddhu.talk()
siddhu.walk()

siddhu.first_name = "siddhu"
siddhu.last_name = "moosewala"

print(siddhu.first_name)
print(siddhu.last_name)

class Hello:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln

    def talk(self):
        print('i am talking')

    def walk(self):
        print("i am walking")

vedant = Hello("vedant","007")
siddu = Hello("siddhu","moosewala")


print(vedant.first_name)
print(vedant.last_name)


print(siddhu.first_name)
print(siddhu.last_name)

vedant.city =""
print(vedant.city)







# Vehicle 
# type model
# start() , stop()

class Vehicle:
    def __init__(self,ty,ml):
        self.type = ty
        self.model = ml


    def start(self):
        print("Start the car")

    def stop(self):
        print("Stop the car")        


Volkswagen = Vehicle("sedan","PoloGT")
Toyota = Vehicle("suv","Fortuner")

print(Volkswagen.type,Volkswagen.model)
print(Toyota.type,Toyota.model)








