# firstname = "vedant"
# print(firstname[0])
# print(firstname[1])
# print(firstname[2])
# print(firstname)



city = "mumbai"
print(len(city))
for c in range(len(city)):
    print(city[c])


greet = "hello"
for g in range(len(greet)):
    print(greet[g])



c = "chandrapur"
i =0 
while( i<len(c)):
    print(c[i])
    i = i + 1



city5 = "ponicherry"
for x in range(len(city5)):
    print(city5[x])



city = "THIRUVANANTPURAM"
i=0
while(i<(len(city))):
    print(city[i])
    i = i + 1


cty = ["ooty","mysore","goa"]
names=["montu","sunny","manshu","monty","vedu"]
for x in range(len(cty)):
    print(cty[x])

i = 0
while(i < len(names)):
    print(names[i])
    i = i + 1 



print("a" in names[2])
print("vedu" in names and "ooty" in cty)
