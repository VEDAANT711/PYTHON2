reclen = 10
with open('cities.bin','wb') as f:
    n = int(input('ENTER THE NUMBER OF CITIES='))
    for x in range(n):
        city = input ('ENTER THE CITY=')
        city = city + (reclen - len(city)) * " " 
        city = city.encode()
        f.write(city)

# reclen = 20
# with open('cities.bin','wb') as f:
#     n = int(input('Enter the number of cities'))
#     for x in range(n):
#         city = input('enter the city') # pune
#         city = city + (reclen - len(city)) * " "
#         city = city.encode()
#         f.write(city)