
#single_Inheritance#

class Father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayname(self):
        print(self.firstname + self.lastname)


class Son(Father):
    def __init__(self,fn,ln,sn):
        super().__init__(fn,ln)
        self.sname = sn 


    def displaySname(self):
        print(self.sname + self.sname)


ved = Son("hie","ssup","bye")
print(ved.firstname)
print(ved.lastname)
ved.displayname()
ved.displaySname()


# Multi-level Inheritance #

class Grandfather:
    def __init__(self,ln,fn):
        self.firstname = fn
        self.lastname = ln

    def displayGname(self):
        print(self.firstname + self.lastname)

class Father(Grandfather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.Fname = ffn

    def displayFname(self):
        print(self.Fname + self.lastname )

class Son(Father):
    def __init__(self, fn, ln, ffn,ssn):
        super().__init__(fn, ln, ffn)
        self.Sname = ssn

    def displaySname(self):
        print(self.Sname + self.lastname)



ved = Son("gaikwad","nemichand","shashikant","vedant")
print(ved.firstname)
print(ved.lastname)
print(ved.Fname)
print(ved.lastname)

ved.displayFname()
ved.displayGname()
ved.displaySname()



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



# multiple inheritance
class Mother:
    def __init__(self,fn,ln):
        print("mother constructor called")
        self.firstName = fn 
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)

class Father:
    def __init__(self,fn,ln):
        print("father constructor called .....")
        self.firstName = fn 
        self.lastName  = ln

    def displayName(self):
        print(self.firstName + self.lastName)


class Son(Mother,Father):
    def __init__(self, fn, ln , ssn):
        super().__init__(fn, ln)
        self.sname = ssn

    def dislaySname(self):
        print(self.sname + self.lastName)


chinmay = Son("shirish","deshpande","chinmay")








