import re
# str = "man map sun mop run"
# result = re.search(r'm\w\w',str)
# if result:
#     print(result.group())


str2 = "man ran sun fun map rap shape mate fate"
list2 = re.findall(r'm\w\w',str2)
print(list2)

str2 = "python is good language to learn"
q3 = re.match(r'p\w\w',str2)
print(q3.group())
if q3:
    q3.group()


import re
str4 = "This ; is the : 'core' python's book"
result = re.split(r'\W+',str4) 
print(result)   

str5 = "i am learning javascriet and javascriet"
q4 = re.sub(r"javascrit","javascript",str5)
print(q4)