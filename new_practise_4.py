city = ["pondicherry","patna","thane","lucknow"]
# for x in city:
#     print(x)

# for i in range(0):
#     print(city(i))    


i1 = 0
while i1 < len(city):
    print(city[i1])
    i1 = i1 + 1


veg = ["brinjal","cabbage","cauliflower","carrot"]
veg.remove("cabbage")
print(veg)


numbers = [11,22,33,44]
numbers.clear()
print(numbers)
numbers.insert(0,99)
numbers.insert(4,33)
numbers.insert(3,00)
numbers.insert(2,77)
numbers.insert(1,66)

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)

print(numbers)

a = [7,0,6,6,5]
b = [5,8,5,3,7]
b.extend(a)
print(b)
















