birthyear = [1992,1924,1945,2005]
ages=[]
for i in birthyear:
    ages.append(2024-i)
print (ages)  

#list_Compherension
a=[2024 - i for i in birthyear]
print(a)

#map
a1=list(map(lambda x : 2024 - x,birthyear))
print(a1)

marks = [43,66,50,78,99,92]
abv50 = []
for x in marks:
    if (x >= 50):
        abv50.append(x)
print(abv50)     

a2=[x for x in marks if x>50]
print(a2)

#filter
b = list(filter(lambda x : x > 50, marks))
print(b)

from functools import *

lst = [1,2,3,4,5]
total = 0
for x in lst:
    total = total + x
print(total)    

#reduce
lst = [11,22,33]
e = reduce(lambda x,y:x+y,lst)
print(e)  

lst2 = [11,22,33]
print(sum(lst2))
print(max(lst2))
print(min(lst2))


e = (total:= total + x for x in lst )
print(e)