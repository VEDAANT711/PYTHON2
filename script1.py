strOne = "13121"
e = strOne.isdigit()
print(e)



strtwo = 'vedan0'
e1 = strtwo.isalpha()
print(e1)


strtwo = ' '
e2 = strtwo.isalnum()
print(e2)


info = 'gaikwadvedant2@gmail.com'
e3 = info.split('@')
print(e3)


info2 = 'i am learning js'
e4 = info2.split('i')
print(e4)

full_name = ('Ninad')
e5  = full_name.istitle()
print(e5)



lastname = "gaikwad"
e6 = lastname.islower()
print(e6)



city = '     '
q = city.isspace()
print(q)



city2 = 'citynagpur'
w = city2.removeprefix('city')
print(w)



city3 = 'citynagpur'
v = city3.removesuffix('nagpur')
print(v)


str1 = "123"
str2 = "12.34"
str3 = "½"
str4 = "Ⅳ"  # Roman numeral 4

print(str1.isnumeric())  
print(str2.isnumeric())  
print(str3.isnumeric())  
print(str4.isnumeric()) 


print(str1.isdigit())  
print(str2.isdigit())  
print(str3.isdigit())  
print(str4.isdigit()) 


