# Single Inheritance

class Son:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname  = ln
    def displyname(self):
        print(self.firstname + self.lastname)  


class Father(Son):
    def __init__(self, fn, ln, ffn):
        super().__init__(fn, ln)
        self.fathername = ffn 
    def displayfname(self):
        print(self.fathername)    

ved = Father("ved","007","shashikant")
print(ved.firstname)
print(ved.lastname)
print(ved.fathername)
ved.displyname()
ved.displayfname()

# Multi-Level Inheritance

class GrandFather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayGname(self):
        print(self.firstname + self.lastname)
       

class Father(GrandFather):
    def __init__(self, fn, ln, ffn):
        super().__init__(fn, ln)
        self.fname = ffn

    def displayFname(self):
        print(self.fname + self.lastname)


class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.Sname = ssn

    def displaySname(self):
        print(self.Sname + self.lastname)
        super().displayGname()
        super().displayFname()

v = Son("h","e","l","o")
print(v.firstname) 
print(v.lastname)
print(v.Sname)
print(v.fname)
v.displayGname()
v.displayFname()
v.displaySname()

# multiple inheritance

class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.fname = fn 
        self.lname = ln

class Father:
    def __init__(self,fn,ln):
        print("father constructor called")
        self.fname = fn 
        self.lname = ln

class Son(Father,Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def Sname(self):
        print(self.sname + self.fname + self.lname)

chinmay = Son("chinmay","shirish","deshpande")

# Herarchical inheritance #

class Mother:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    
    def displayMname(self):
        print(self.firstname + self.lastname)
        
class Daughter(Mother):
    def __init__(self, fn, ln,ddn):
        super().__init__(fn, ln)
        self.dname = ddn

    def displayDname(self):
        print(self.dname + self.lastname)

class Son(Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def displaySname(self):
        print(self.sname + self.lastname)


vedu = Son("varsha","gaikwad","vedant")
sid = Daughter("varsha","karlekar","siddhant")
print(vedu.firstname)
print(vedu.lastname)
print(vedu.sname)
vedu.displayMname()
vedu.displaySname()

print(sid.firstname)
print(sid.lastname)
print(sid.dname)
sid.displayMname()
sid.displayDname()