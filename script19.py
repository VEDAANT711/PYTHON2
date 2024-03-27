

class Mother:
    def __init__(self,fn,ln):
        print("Mother Constructor Called....")
        self.firstname = fn
        self.lastname = ln
    
    def displayname(self):
        print(self.firstname + self.lastname)


class Father:
    def __init__(self,fn,ln):
        print("Father Constructor called....")
        self.firstname = fn
        self.lastname = ln

    def displayname(self):
        print(self.firstname + self.lastname)


class Son(Father,Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displayname(self):
        print(self.sname + self.lastname)
ved = Son("shashi","varsha","ved") 
ved.displayname()               



# class  Calci:
#     def add (self,a,b):
#         print(a+b)

#     def add (self,a,b,c):
#         print(a,b,c)

#     def add (self,a,b,c,d):
#         print(a,b,c,d)

# cal = Calci ()      
# # cal.add(23,44)
# # cal.add(34,55,67)
# Calci.add(22,45,67,87)      


class Calcu:
    
  def add (self, a = None, b = None, c = None, d = None):
    if(a != None and b != None and c != None and d != None):
        print(a+b+c+d)
    elif(a != None and b != None and c != None):
        print(a+b+c)
    elif(a != None and b != None):
        print(a+b)


cal = Calcu ()      
Calcu.add(44,56,78,34)
Calcu.add(34,33,43)
Calcu.add(23,44)
Calcu.add(23)
     




