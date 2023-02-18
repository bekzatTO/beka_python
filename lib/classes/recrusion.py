import os,sys,pdb






# def factorial(x):


#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))


# num = 3
# print("The factorial of", str(num), "is", factorial(num))


# d=4

# def factorial(x):
#     while True:
#        # pdb.set_trace()
#         if x==1:
#             return 1
#         else:
#             return  x * factorial(x-1)
        
# print(factorial(d))


# Memoization is the process of caching values so it makes running script much faster & you can use built in python tool lru_cache decorator



# Messy fibonacci  
cache={}
try:
    def fibonacci(n):
        
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

except TypeError:
    print("Must be positive integer")




        



    

