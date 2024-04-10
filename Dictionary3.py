i = {
    "firstname" : "vedant",
    "lastname"  : "gaikwad",
    "rollno"    : 74,
    "age" : 24     
}

print(i['firstname'])
print(i.get('lastname'))
y = i.setdefault('city',"pune")
print(y)
print(i)



students = [
    {
        "firstName":"chinmay",
        "lastName":"deshpande",
        "age":34,
        "skills":["html","css","js"]
    },
    {
        "firstName":"raj",
        "lastName":"kumar",
        "age":32,
        "skills":["html","css","js","python"]
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":23,
        "skills":["html","css","js"]
    }

]


for x in students:
    if "python" in x['skills']:
        print(x['firstName'])

for x in students:
    print(x['firstName']+":"+str(len(x['skills'])))        



total = 0
for m in students:
    total = total + x['age']
print(total/len(students))













