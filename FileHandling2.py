# f = open('hi.py','a+')
# while str != "@":
#     str = input("Enter the names ")
#     if str != '@':
#         f.write(str + "\n")
# f.seek(0,0)
# str2 = f.read()
# print(str2)
# f.close()

import os, sys
# fname = input("Enter the Name = ")
# if os.path.isfile(fname):
#     f = open(fname,'r+')
# else:
#     sys.exit()
# print('The File Content are given below: ')
# str = f.read()
# print(str)
# f.close()        




fname = input("Enter File Name")
if os.path.isfile(fname):
    f = open(fname,'r+')
else:
    print('file does not exist') 
    sys.exit() 
    
cc = 0
cw = 0
cl = 0

for line in f:
    cl = cl + 1
    list = line.split() 
    cw = cw + len(list)
    cc = cc + len(line)
print(cl)
print(cw)
print(cc)

f.close()  






