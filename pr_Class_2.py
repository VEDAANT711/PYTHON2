# # get set
# class Hie:
#     def setfn(self,fn):
#         self.fn = fn
#     def getfn(self):
#         return self.fn
    
#     def setln(self,ln):
#         self.ln = ln
#     def displyname(self):
#         print(self.fn+self.ln)


# ved = Hie() 
# ved.setfn('ved')
# ved.setln('007')
# ved.displyname()       

    
# #constructor 

# class Person:

#     country = "India"

#     def __init__(self,fn,ln):
#         self.fn = fn
#         self.ln = ln

# #ClassLevelMethod

# @classmethod

# def changeCountry(cls):
#     cls.country = "Bharat"

# #InstanceLevelMethod

# def displayName(self):
#     print(self.fn+self.ln)


# ved = Person("ved","007")
# vedu = Person("vedu","007")       
# print(ved.country) 
# ved.country = 'bharat'
# print(ved.country)

class Emp:
    Count = 0
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
        Emp.Count = Emp.Count + 1
        
    @staticmethod
    def  countObj():
        return Emp.Count
    
emp1 = Emp("ved","007")
emp2 = Emp("vedu","don")
emp3 = Emp("vedant","gaikwad")
e = Emp.countObj()
print(e)