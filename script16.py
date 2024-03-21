class Person:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln

    def display_name (self):
        print(self.first_name  + self.last_name)


vedant = Person("vedant","gaikwad")
siddhu = Person("siddhu","mooewala")


print(vedant.first_name)
print(siddhu.first_name)





class Language:
    def __init__(self,js,py,j,p):
        self.javascript = js
        self.python = py
        self.J = j
        self.P = p

        

    def display_name(self):
        print(self.javascript + self.python + self.J +self.P) 


skill1 = Language("objects & ","arrays"," are from Javascript"," THANKYOU")
skill2 = Language("Dictionary &","lists"," are from Python"," THANKYOU")
# print(skill1.javascript)
# print(skill1.python)
# print(skill2.javascript)
# print(skill2.python)
skill1.display_name()
skill2.display_name()



class Person2:
    country = "India"
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
    def display_name(self):
        print(self.first_name + self.last_name)
        

    @classmethod
    def changeCountry(cls,cntry):
        cls.country = cls
            
vedu = Person2 ("vedu","007")
siddhu = Person2 ("siddhu","moosewala")
monty = Person2 ("meetha","lesh")

print(vedu.first_name,vedu.last_name)

print(siddhu.first_name,siddhu.last_name)

print(monty.first_name,monty.last_name)

monty.country = "Pakistan"

print(monty.country)

Person2.changeCountry = "Srilanka"
print(vedu.country)
print(siddhu.country)





