

print('hello'+'bye')
print(1 + 2)
print([11,22,33] + [44,55,66])



class Book1:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,others):
        return self.pages + others.pages

class Book2:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,others):
        return self.pages + others.pages   

ramayan = Book1(150)
mahabarat = Book2(90)

print(ramayan.pages + mahabarat.pages)
print(ramayan + mahabarat)

print(mahabarat + ramayan)  




class BookA:
    def __init__(self,pages):
        self.pages = pages

    def __gt__(self,others):
        return self.pages >  others.pages    


class BookB:
    def __init__(self,pages):
        self.pages = pages

    def __lt__(self,others):
        return self.pages > others.pages
        


ram = BookA(130)
sham = BookB(34)

#print(ram.pages > sham.pages)
print(ram > sham)
print(sham<ram)



class WorldBank:
    def loan(self):
        print("I am Loan from WorldBank")
    def save(self):
        print("I am save from WorlBank") 


class SBI(WorldBank):
    def loan(self):
        print("I am loan from SBI")
        super().loan()
    def save(self):
        print("I am Save from SBI") 
        super().save()

class PNB(WorldBank):
    def loan(self):
        print("I am Loan from PNB")
        super.loan()
    def save(self):
        print("I am Save from PNB")
        super.save()

a = SBI()
a.loan()
a.save()





class Tata:
    def Engine(self):
        print("I am Engine from Tata")
    def Milage(self):
        print('I am Milage from Tata')

class Punch(Tata):
    def Engine(self):
        print("I am Engine from Punch")
        super().Engine()
    def Milage(self):
        print('I am Milage from Punch')
        super().Milage()
    

class Harrier(Tata):
    def Engine(self):
        print("I am Engine from Harrier")
        super().Engine()
    def Milage(self):
        print('I am Milage from Harrier')
        super().Milage()
      
a = Punch()
a.Engine()
a.Milage()

b = Harrier()
b.Engine()
b.Milage()