info3 = {

    "firstName":"vedant",
    "lastName":"gaikwad",
    "rollNo":74,
    "age":23
}
print(info3.get('firstName'))
y = info3.setdefault('city',"bengaluru")
print(y)
print(info3)



cricket =[
{
    "Firstname" : "Virat",
    "Lastname" : "Kohli",
    "Century"  : 80,
    "Spouse"   : "Anushka Sharma" 
},
{
    "Firstname" : "Rohit",
    "Lastname"  : "Sharma",
    "Century"   : 47,
    "Spouse"    : "Ritika Shajda"
},
{
    "Firstname" : "Mahendra Singh",
    "Lastname"  : "Dhoni",
    "Century"   : 16,
    "Spouse"    : "Sakshi Singh" 
}
]
print(cricket[2])

for c1 in cricket:
    print(c1['Firstname'])

for x in cricket:
    if "Anushka" in x['Spouse']:
        print(x['Firstname'])  

for x in cricket:
    "IPL trophy" in cricket[0] 
    print(cricket)



        
Market =[
{
    "item1" : "Biscuit",
    "item2" : "Chips",
    "billno."  : 123,
    "bill"   : 50 
},
{
    "item3" : "Milk",
    "item4" : "Sugar",
    "billno."  : 124,
    "bill"   : 75
},
{
    "item5" : "Bread",
    "item6" : "Butter",
    "billno."  : 125,
    "bill"   : 100 
}
]

#for x in Market:
#    if x['bill'] > 50 and str("123") in x["billno."]:
 #       print(x['item6'],x['billno.'])


#for x in Market:
#   print(x['item1']+":"+ (len(x['bill'])))























