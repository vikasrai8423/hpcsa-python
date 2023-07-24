# function without a return statement 
def my_functionname():
    print("I am printing some value")
    

return_val = my_functionname()    
print("Returned value from the function is " , return_val)


#function with a return statement 
def my_functionname():
    print("I am printing some value")
    return 1 
    
return_val = my_functionname()    
print("Returned value from the function is " , return_val)



#function with a return statement and input parameters
def my_addition_function(num1,num2):
    return num1+num2

my_first_number = 1
my_second_number = 2 

return_val = my_addition_function(my_first_number,my_second_number)
print("Returned value from my_addition_function is ", return_val)


#function with default value from a literal 
def my_addition_function(num1=11,num2=10,num3=90):
    return num1+num2+num3

return_val = my_addition_function(11, num3=100,num2=10)
print("Returned value from my_addition_function is ", return_val)

