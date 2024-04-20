# reclen = 10
# with open('cities.bin','wb') as f:
#     n = int(input('ENTER THE NUMBER OF CITIES='))
#     for x in range(n):
#         city = input ('ENTER THE CITY=')
#         city = city + (reclen - len(city)) * " " 
#         city = city.encode()
#         f.write(city)

reclen = 20
with open('cities.bin','wb') as f:
    n = int(input('Enter the number of cities: '))
    for x in range(n):
        city = input('enter the city: ') # pune
        city = city + (reclen - len(city)) * " "
        city = city.encode()
        f.write(city)


# reclen = 20
# try:
#     with open('cities.bin','rb') as f:
#         n = int(input('record number'))
#         f.seek(reclen * (n-1))
#         str = f.read(reclen)
#         str = str.decode()
#         print(str)
# except FileNotFoundError:
#     print("File not found")



    

reclen = 20
try:
    with open('cities.bin', 'rb') as f:
        n = int(input('Enter the record number: '))
        f.seek(reclen * (n - 1))
        data = f.read(reclen)
        city = data.decode().strip()  # Remove any trailing whitespace
        print("City:", city)
except FileNotFoundError:
    print("File not found.")
except ValueError:
    print("Invalid record number. Please")



# reclen = 20
# with open('cities.bin','rb') as f:
#     n = int(input('record number')) # 1
#     f.seek(reclen * (n-1))
#     str = f.read(reclen)
#     str = str.decode().strip()
#     print("str:",str)
