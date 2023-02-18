import os,sys


try:
    f=open("python.py")
    
except FileNotFoundError:
    print("It doesn't exist lil bro")

except Exception: #  When writing excepts, make sure to write the more specific error types first and then the more general ones
   print("Idk what the error is")



