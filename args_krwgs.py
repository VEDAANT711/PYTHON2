def add(*args):
    print(args)
add(1,22,33,4,5,6,7,3,3)


def decorator(func):
    def wrapper(*args,**kwargs):
        print("function")
        return func(*args,**kwargs)
    return wrapper
@decorator
def greet(*name,**kwargs):
    print(f'hi {name}') 

greet(1,2,3,4,5,a=22,b=34)  


def say_hello():
    return "hello"
print(say_hello())


# def outer():
#     def inner():
#         print("inner is called")
#     inner()
# outer()


def outer ():
    def inner():
        print("inner is called")
    return inner
e= outer()
e()


def decorator_function(func):
    def wrapper_function():
        print("before is called")
        func()
        print("outer is called")
    return wrapper_function

@decorator_function
def say_hello():
    print("say hello") 

# a= decorator_function(say_hello)
# print (a)          
# a()

def decorator(func):
    def wrapper(*args,**kwargs):
        print("function")
        return func(*args,**kwargs)
    return wrapper
@decorator
def calculate(*args,**kwargs):
    print(args) 
    print(kwargs)

calculate(1,2,3,4,a=2,b=3)  


def upperCase_decorator(func):
    def wrapper(*args,**krwags):
        e= func(*args,**krwags)
        return e.upper()
    return wrapper


def star_decorator(func):
    def wrapper(*args,**krwags):
        e = func(*args,**krwags)
        return f'*** {e}***'
    return wrapper

@star_decorator
@upperCase_decorator
def greet(word):
    return f'helllo {word}'

print(greet('vedant'))