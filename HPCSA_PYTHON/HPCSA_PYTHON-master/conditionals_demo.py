"""
# only if 
if condition1 :
   executes when the condition1 is true

# if else 
if condition1 :
   executes when the condition1 is true
else :
   executes when the condition1 is false
   
#if elif else ladder   
if condition1 :
   executes when the condition1 is true
elif condition2 :
   executes when the condition2 is true and condition1 is false
else :
   executes when the both condition1 and condition2 is false

"""   
"""
if the number is divisible by 3 print Fizz    
if the number is divisible by 5 print Buzz
if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

Testcase : 
    21 --> Fizz
    50 --> Buzz
    15 --> Fizz Buzz
    22 --> Invalid Input 
"""
# # solution1 
# input_num = int(input("please enter a number"))

# remainder_from_3 = input_num%3
# remainder_from_5 = input_num%5

# if remainder_from_3==0 and remainder_from_5 ==0 : 
#     	print(" Fizz Buzz")
# elif remainder_from_3 == 0 :
# 	print("Fizz")
# elif remainder_from_5 == 0 :
# 	print("Buzz")


	
# # solution2 
# num = int(input("Please enter the number"))


# if num %5==0 and num % 3 ==0 :
#     print("Fizz Buzz")
# elif num%3 == 0 :
#     print("Fizz")
# elif num%5 == 0 :
#     print("Buzz")
# else:
#     print("Invalid Input")
    

# # solution3
# num = int(input("Please enter the number"))
 
# if num %5==0  :
#     if num % 3 ==0 : 
#         print("Fizz Buzz")
#     else:
#         print("Buzz")    
# elif num%3 == 0 :
#     print("Fizz")
# else:
#     print("Invalid Input")


# # solution4
# num = int(input("Please enter the number"))    
# if num %3==0  :
#     if num % 5 ==0 : 
#         print("Fizz Buzz")
#     else:
#         print("Fizz")    
# elif num%5 == 0 :
#     print("Buzz")
# else:
#     print("Invalid Input")     


# solution5
num = int(input("Please enter the number"))

# very specific to python
is_inside_if_clause = 'N'
if num%3 == 0 :
    print("Fizz",end = ' ' )
    is_inside_if_clause = 'Y'

if num%5 == 0 :
    print("Buzz")
    is_inside_if_clause = 'Y'

if  is_inside_if_clause != 'Y':
    print("Invalid Input")


