# import random, os,sys, pdb


# correct=random.randrange(1,11)

# i=1



# while i < 4:
#   #  pdb.set_trace()
#     def if_wrong(x,i):
#         if x > 10:
#             i=i-2
#             print("The number you have selected is higher than the range given, please try again and we'll refund your try")
            
#         elif x <= 0:
#             i=i-2
#             print("The number you have selected is lower than the range given, please try again and we'll refund your try")
#         return
#     chosen=int(input("Try to guess the number: "))
#     if_wrong(chosen,i)
    

#     if chosen == correct:
#         print("congrats you got right number")
#         break
#     else:
#         print("try again")
#     i+=1
#     if i == 4:
#         print("you have used all of you chances")







# def numba(x): # when a function calls itself to reuse its own parmeters
#   if x>0 :
#     result = x+numba(x-1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\nRecursion Example Results")
# numba(6)








 





# tries=3

# while tries != 0:
#     if chosen < correct:
#         tries=tries-1
#         print( f"Oops, try again!!! Your guess was too low: You have {tries} guesses left")
#         chosen=int(input("Try to guess the number: "))
#     elif chosen > correct:
#         tries=tries-1
#         print(f"Oops, try again!!! Your guess was too high: You have {tries} guesses left")
#         chosen=int(input("Try to guess the number: "))    
#     elif tries == 0:
#         print("No more tries")
        
#     else:
#         print("Hooray!!! You got it")
        

    


