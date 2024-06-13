# def add (x,y):
#     return x + y
# r = add (12,3)
# print(r)



# def greet (name):
#     return "hello" + name
# t = greet(" vedu")
# print(t)


#args

def add (*args):
    print(args)
    total=0
    for i in args:
        total = total + i
    return total    
t = add(11,22,33,44)
print(t)


def info (**kwargs):
    #print(kwargs)
    kwargs['city']="pune"
    return kwargs
r = info(name="vedu",age = "23",city="nagur")
print(r)

#lambda function 
#function as parameter to another function

add = lambda a,b:a+b
def addition (fn,a,b):
    e = fn(a,b)
    return e
r = addition (add,1333,85675980)
print(r)

m = lambda i,j:i*j
def mul (fn,i,j):
    k = fn(i,j)
    return k
e = mul (m,45,665)
print(e)




d=lambda p,q:p/q
def div (fn,p,q):
    a=fn(p,q)
    return a
b=div(d,89,34)
print(b)





