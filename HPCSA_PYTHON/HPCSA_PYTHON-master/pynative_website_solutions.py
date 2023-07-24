#Exercise 1: Print First 10 natural numbers using while loop

def print_num(higher_limit):
    i = 1
    while(i<=higher_limit):
        print(i , end = ' ')
        i = i+1

# print_num(10)

# Exercise 2: Print the following pattern
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


# for row in range(0,int(input("rows: "))+1):
#     print_num(row)
#     print('')

# #Exercise 4: Write a program to print multiplication table of a given number

# for row in range(0,11):
#     print(2*row)
    
# #Exercise 6: Count the total number of digits in a number    
# cnt = 0 
# inp_number = int(input("enter number :"))
# while(inp_number):
#     inp_number = inp_number//10
#     cnt = cnt+1
# print("No of digits " , cnt )    

# Exercise 7: Print the following pattern
# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

# def print_reverse_num(higher_bound):
#     for num in range(higher_bound,0,-1):
#         print(num , end = ' ')

# input_row = int(input("rows: "))    
# for row in range(input_row,0,-1):
#      print_reverse_num(row)
#      print('')

# #Exercise 9: Display numbers from -10 to -1 using for loop
# for row in range(-10,0,1):
#     print(row , end = ' ')
    
#Exercise 10: 
# Use else block to display a message “Done” after successful execution of for loop    

# for row in range(-10,0,1):
#     print(row , end = ' ')
#     break
# else:
#     print("Done")    

# row = -10
# while(row<0):
#     print(row , end = ' ')
#     row = row+1
#     break
# else:
#     print("Done") 

#Exercise 12: Display Fibonacci series up to 10 terms

# num1 = -1
# num2 = 1
# for i in range(0,int(input("how many terms ")),1):
#     sum = num1 +num2 
#     print(sum , end = ' ')
#     num1 = num2
#     num2 = sum

#Exercise 13: Find the factorial of a given number    

# mult = 1
# for i in range(int(input("number : ")) , 0 , -1):
#     mult = mult*i
# print("Factorial " , mult)    

#Exercise 14: Reverse a given integer number
# Given: 76542  Expected output: 24567

# def extract_digits_from_end(inp_number):
#     while ( inp_number):
#         print( inp_number%10 )
#         inp_number = inp_number//10

# extract_digits_from_end(76542)

# new_number = 0 
# inp_number = int(input("Number : "))
# while ( inp_number):
#         digit = inp_number%10 
#         new_number=  new_number * 10 + digit
#         inp_number = inp_number//10
# print(new_number)


# Exercise 16: Calculate the cube of all numbers from 1 to a given number

# for i in range(1,int(input("number : "))+1  , 1):
#     print(f"Current Number is : {i}  and the cube is {i**3}")

# def print_triangle(higher_limit):
#     i = 1
#     while(i<=higher_limit):
#         print('*' , end = ' ')
#         i = i+1
    
# def print_reverse_triangle(higher_bound):
#      for num in range(higher_bound,0,-1):
#         print('*' , end = ' ')

# inp_rows = int(input("Please enter number of rows "))//2
# for row in range(1,inp_rows+2):
#     print_triangle(row)
#     print('')

# for row in range(inp_rows,0,-1):
#      print_reverse_triangle(row)
#      print('')    

total_rows = int(input("rows : "))     
for i in range(1,total_rows+1):
    for space in range(0,total_rows-i):
        print(" ", end = '')
    for star in range(0,2*i-1):
        print( "*",end = '')    
    print('')
        