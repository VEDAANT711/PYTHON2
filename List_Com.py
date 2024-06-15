# by = [1989,1990,1991,1992]
# a = []
# for i in by:
#     b = 2024-i
#     a.append(b)
# print(a)

# a1 = [2024-i for i in by]
# print(a1)
 
mrks = [77,68,90,54,61,48,35]
ab50=[]
for i in mrks:
    if (i > 70):
        ab50.append(i)
print(ab50)    

a2=[i for i in mrks if(i>50)]
print(a2)

listE = [45,66,33,44,56,32,47,12]
oddEven=[]
for x in listE:
    if x % 2 == 0:
        oddEven.append("Even")
    else:
        oddEven.append("Odd")

print(oddEven)


a3=["even" if x % 2 == 0 else "odd" for x in listE]
print(a3)


list=[1,2,3,4,5,6,7,8,9,10]
a=[]
for i in range(2,21,2):
        a.append(i)
print(a)        

b=[i for i in range(2,21,2)]
print(b)

c=[i for i in range(50,4,-5)]
print(c)





