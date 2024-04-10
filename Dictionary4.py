info = ["vedant","gaikwad",23,44]

print(info[0])

info[0]="vedu"
print(info[0])

info.append("pune")
print(info)

info.remove("gaikwad")
print(info)



info2 ={

    "firstname":"vedant",
    "lastname":"gaikwad",
    "age":"23",
    "rollno":"19011144"
}
print(info2)
print(type(info2))
print(info2["firstname"])
info2['firstname']="vedu"
print(info)
info2['city'] = "nagpur"
print(info2)
info2.pop('age')
print(info2)
info2.popitem()
print(info2)


human = {
    "height":"185",
    "weight":"75",
    "color":["Wheatbrown","albino","melaninated"]
}
human['BMR'] =22.7
print(human)
human['color'.pop(0)]
print(human)



