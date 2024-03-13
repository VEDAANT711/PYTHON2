def add(x,y):
    return x + y
e = add(33,54)
print(e)



lambda x,y : x+y 
f = add(22,45)
print(f)



add = lambda x : x*x
print(add(44))



a = lambda x,y : x+y
def add(fn,x,y):
    f = fn(x,y)
    return f
e1 = add(a,12,43)
print (e1)




sub  = lambda x,y:x-y 
def subtraction(fn,s,t):
    fn = lambda x,y:x-y 
    e = fn(s,t)
    return e   
e2 = subtraction(sub,12,6)
print(e2)




def add():
    return lambda x,y :x+y
e = add()
print(e)
e2 = e(12,3)
print(e2)






















