# import scripts

# print(   scripts.__name__  )
# print(   scripts.__file__  )



# class Family(object):

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

    



#     def __repr__(self):
#         return "This class prints developer's chapter"
    
#     def __str__(self):
#         return f"This class is about our familly {__name__}, {__class__}"
    



#     def member(self):
#         return f"My name is {self.name}, and i'm {self.age} {__file__} {__name__}"









# p1 = Family("miki", 42)
# print(p1.member())



# class Parent:
#     def __init__(self, name):
#         self.name=name
        
#     def display2(self):
#         print("Name:", self.name)

# class Child(Parent):
#     def __init__(self,age,name):
#         self.age=age
#         super(Child,self).__init__(name)
        
       
#     def display(self):
#         print("Age:", self.age)
#         print("Name:",self.name)

# c = Child(16,"Bekzat")
# print(c.display())

balance=500
class Clothing:
    def __init__(self, shoes,pants,shirt,person):
        self.shoes=shoes
        self.pants=pants
        self.shirt=shirt
        self.person=person
        

    def shoe_fit(self):
        if self.person >= 16:
            if self.shoes<10.5:
                return "Shoes too small"
            elif self.shoes>=10.5:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10"
    def pants_fit(self):
        if self.person >= 16:
            if self.pants<33:
                return "Shoes too small"
            elif self.pants>=33:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10"

    def shirt_fit(self):
        if self.person >= 16:
            if self.shirt<18:
                return "Shirt too small"
            elif self.shirt>=18:
                return "Fits perfectly"
        else:
            return "Your shoe size is from a kids 10 to an adults 10" 
class Buy(Clothing):
    def __init__(self,year=None, shoes=None ,pants=None,shirt=None,person=None):
        self.year = year        
        Clothing.__init__(self,shoes,pants,shirt,person)

    def purchase(self):
        if self.shirt_fit() or self.pants_fit or self.shoe_fit == False:
            return "I have enough money to buy almost everything I want :D"
        else:
            return "I can't buy everything!"
        
p1=Buy(2006,11,18,18,12)
print(p1.purchase())





cache={}

class Rec():
    def __init__(self,n):
        self.n=n

        def fibonacci(n):
            try:        
                if n in cache:
                    return cache[n]
                if n == 1 or n == 2:
                    value = 1 
                    return value
                elif n > 2:
                    value = fibonacci(n-1) + fibonacci(n-2)
                    cache[n]=value
                    return value
        
                for n in range(1,101):
                    print(n,";   ", fibonacci(n))

            except Exception as a:
                print("Must be positive integer")




        
