#Create Object
# f = open('hi','w')
# str = input("Enter the Name =")
# f.write(str)
# f.close()


# f = None
# try: 
#     fileName = input('Enter the FileName')
#     f = open(fileName,'r')
#     str = f.read()
#     print(str) 
# except FileExistsError:
#     print("File not found")
# finally:
#     if f is not None:
#         f.close()
# print("BYE!")        


f  = open('hi.py',"w")
while str != "@":
    str = input('Enter the name '+'\n')
    if str != '@':
        f.write(str + '\n')
f.close()                   
                
