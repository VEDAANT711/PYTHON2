class Bank:
     country = "INDIA"
     Count = 0

     def __init__(self,fn,ln,acc,bal):
          self.firstname = fn
          self.lastname = ln
          self.account = acc
          self.balance = bal
          self.transctions  = []
          Bank.count = Bank.count + 1



     def deposite(self,amount):
        self.balance = self.balance + self.amount
        self.transctions.append(amount)
        print("Amount Deposited Successfully")


     def withdrawal(self,amount):
         if(self.balance > amount):
            self.balance = self.balance - self.amount
            self.transctions.append(-amount)
         else:
             print("Insufficient Balance")  

     def LastTransctions(self,x):
         return self.transctions[-x::]
     

     @classmethod
     def ChangeCountry(cls,cl):
         cls.country = cl


     @staticmethod
     def ObjCount():
         return Bank.count    
     




     

























