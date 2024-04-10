list1 = [1989,1990,1991,1992]
ages = []
 
for x in list1:
    i = 2024 - x
    ages.append(i)
print(ages,"by in operator")



a = list(map(lambda x:2024-x,list1))
print(a, "by lambda function")

print([2024 - i for i in list1],"by ternery operator")



f = lambda x : 2024 - x
f(list1[0])


names = ["Chinnaswami venugopal iyer","sarika","kajal","ninad"]
above5 = []
for x in names:
    if len(x)>5:
        above5.append(x)
print(above5,"by in op")        
 

print([x for x in names if len (x) > 5], "by ternary") 

e = list(filter(lambda x: len(x) > 5,names))
print(e, "by lambda fn")


a = [2,3,-4,5,-6,7,8,22,-33,44,55,66666,-77]
t=[]
for x in a:
    if x > 0:
        t.append("wihdrawal")
    else:
        t.append("deposite")  
print(t)          

print(list(filter(lambda x : x > 0 , t)))
