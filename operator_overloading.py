# print("hello"+"world")
# print(12 + 12)

# class BookX:
#     def __init__(self,pages):
#         self.pages  = pages

#     def __add__(self,other):
#         return self.pages + other.pages
    
# class BookY:
#     def __init__(self,pages):
#         self.pages = pages

# ramayan = BookX(120)
# mahabharat = BookY(40)
# print(mahabharat)
# print(ramayan.pages)

# program3 


class BookX:
    def __init__(self,pages):
        self.pages  = pages

    def __gt__(self,other):
       return self.pages > other.pages

class BookY:
    def __init__(self,pages):
        self.pages = pages

a = BookX(120)
b = BookY(60)

print("A has more pages") if a.pages > b.pages else print('B has more pages')

print("A has more pages") if a > b else print('B has more pages')