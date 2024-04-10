first_name = "vedant"
print(first_name)
e = first_name.upper()
print(e)

last_name = "GAIKWAD"
e2 = last_name.lower()
print(e2)


middle_name = "shashikant"
e3 = middle_name.isupper()
print(e3)

e4 = middle_name.islower()
print(e4)
city = "pune"
e5 = city.startswith("pu")
print(e5)

e6 = city.endswith("NE")
print(e6)

city1 = "QUALALAMPUR"
e7 = city1.count("L")
print(e7)

city2 = " gadchorili "
print(len(city2))
e8 = city2.lstrip()
print(e8)
e9 = city2.rstrip()
print(e9)
e10 = city2.strip()
print(e10)


info ="i am great learner"
e11 = info.replace("learner","sportsmen")
print(e11)


info = ["vedant","gaikwad","7066558537"]
e5 = "@".join(info)
print(e5)

email = "gaikwadvedant2@gmail.com"
e6 = email.split('@')
print(e6)

email = "gaikwadvedant2@gmail.com"
e6 = email.find('a',2)
print(e6)

#removeprefix

email2 = "gmail.com@chinmay"
email3 = "gmail.com@sham"
email4 = "gmail.com@samay"

student = [email2,email3,email4]
lista = []
for x in student:
    q1 = x.removeprefix("gmail.com@")
    lista.append(q1)
print(lista)



















