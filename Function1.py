def addOne(x,y):
    return x + y
e = addOne(12,3)
print(e)



def subTwo(x,y):
    return x - y
f = subTwo(12.3,12.1)
print(f)




def canDrive(age,haveVehicle):
    if age > 18 and haveVehicle:
       return True
    else: 
        return False
g = canDrive(19,True)
print(g)    




def greet (name):
    return( "NAMASTEY "+name)
j = greet("VEDANT")
print(j)





n = ["a","b","c","d","e"]
def names(lst):
    lst.append("f")
    return lst
k = names(n)
print(k)




info = {
    "firstName":"vedant",
    "lastName":"gaikwad"
    #city:pune
}
def addCity(information):
    information['city'] = "nagpur"
    return information
l = addCity(info)
print(l)




numbers = (11,22,33)
def addValue(tupA):
    tupA = list(tupA)  
    tupA.append(44)  
    tupA = tuple(tupA) 
    return tupA
l = addValue(numbers)
print(l)





setA = {11,22,33}
def addElement(seta):
    seta.add(44)
    return seta
z = addElement(setA)
print(z)