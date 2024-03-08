e = dict.fromkeys(["titan","fastrack","sonata"])
print(e)


info ={
    "admin" : "vedant",
    "custom" : "sameer",
    "support": "raj"
}

info.setdefault("manager",None)
print(info)

f = dict.fromkeys(["key1","key2","key3"])
print(f)



strA = 'amol'
print(strA)
print(type(strA))

name = ["chinmay","sarika","rohit"]
print(name)
print(type(name))


info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
print(info)
print(type(info))


#------------------------->

flower = ['lily','sunflower','orchid']
flower2 = ('lily','rose','orchid')
print(flower,flower2)
flower[0] ='rose'
print(flower)
print(flower2)


tupleA = ("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[0])



for x in range(3):
   
    print(tupleA[x])



for t in tupleA:

    print(t)


i = 0
while (i < 3):
    print(tupleA[i])
    i = i + 1


tupleB = 12,23
print(type(tupleB))


tupleC =(11,22,33)
a,b,c=tupleC
print (a)
print (b)
print (c)



tupleF = (11,22,33)
len(tupleF)
e=list(tupleF)
e=tuple(e)
print(e)



d = (11,22,33,44,44)
print(d)
e2 = d.count(44)
print(e2)




e3 = d.index(22)
print(e3)
print(33 in d)


#using constructor

my_tuple = tuple((1,2,3))
print(my_tuple)










