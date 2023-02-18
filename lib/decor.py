import os,sys, time, logging


# def choco(candy):
#     def wrapper():
#         print( "~~~~~~~~~~~~~~~~")
#         candy()
#         print("~~~~~~~~~~~~~~~~~~~~~")
#     return wrapper

# def caramel(candy):
#     def wrapper():
            
#         print("^-^-^-^-^")
#         candy()
#         print( "^-^-^-^-^-^-^-^")
#     return wrapper

# def cookie(candy):
#     def wrapper():

#         print("---------------")
#         candy()
#         print( "-------------------")
#     return wrapper
    
# @choco
# @caramel
# @cookie
# def candy():
#     print("Twix")

# candy()






# def do_twice(func):
#     def wrapper():
#         func()
#         print("Now you can go outside and play\n")
#         func()
#     return wrapper


# @do_twice
# def dress_kids():
#     print("~~~~~~~~~~~~~~")
#     print("kid")
#     print("~~~~~~~~~~~~~~")
#     return


# dress_kids()


# def timer_decorator(func):
#     def wrapper(*args, **kwargs): # *args is an argument that can take and unknown amount of arguements that are numbers usually
#         # **kwargs take an unknown amount and they usualy take words or keys
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f'{func.__name__} took {end - start} seconds')
#         return result
#     return wrapper

# @timer_decorator
# def complex_operation():
#     time.sleep(1)

# complex_operation()



# names = ["Beka","Azat","Sezim"]
# d={}

# def taker(func):
#     def wrapper():    
#         for i,k in enumerate(func()):
#             print(i,k)
        
#     return wrapper

# def laker(d):
#     print(d.items())


# @taker
# def imya():
#     return names

# imya()






# def list_arg_decorator(func):
#     def wrapper(lst):
#         print("The list passed to the function is:", lst)
#         return func(lst)
#     return wrapper

# @list_arg_decorator
# def my_function(lst):
#     print("The list inside the function is:", lst)

# my_list = [1, 2, 3]
# my_function(my_list)

# print(__name__)



# def logger(func):
#     import logging
#     logging.basicConfig(file="{}.log".format(func.__name__), level=logging.INFO)
    


muffins=0
pie=0
money=0
class Sweets():
    def __init__(self,sugar,egg,flour,milk):
        self.sugar=sugar
        self.egg=egg
        self.flour=flour
        self.milk=milk

    def typeOfsweets(self):   #Sugar is measured in teaspoons, milk and flour in cups
        if self.sugar == 9 and self.egg == 1 and self.flour == 2 and self.milk == 1:
            muffins=muffins+6
            return "You have enoughto make half a dozen of muffins"
            
        elif self.sugar == 14 and self.egg == 3 and self.flour == 3 and self.milk == 2:
            pie=pie+1
            return "You can make a pie"
        
    @staticmethod
    def money():
        if muffins >5:
            money= muffins*2.5
            return money
        elif pie==1:
            money=pie*10


p1=Sweets(9,1,2,1)
print(p1.money())



class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * radius * radius

print(Circle.area(10))

        




        



