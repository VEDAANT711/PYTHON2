names=['sarika','poorva','ram','sham']
# print(names)
names2 = names
names2[0]="gippy"
print(names2)
print(names)


cities = ['pune','nagpur','goa']
cities2 = cities.copy()
cities2[0]='wardha'
print(cities)
print(cities2)


country = ['india','srilanka','china','cuba']
country.pop()
country.pop(2)
country.remove('india')
print(country)


numbers = [11,22,33,44]
numbers.append(4444)
numbers.insert(2,9999)
numbers.extend([77,66,88])
print(numbers)


fruits = ["apple","banana","grapes","papaya","apple" , "berry"]
y=fruits.count('apple')
print(y)

g = fruits.index('papaya')
print(g)


fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)
