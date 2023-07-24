# functions are first class citizens 
# var = 10 
# def print_name(first_name,last_name):
#     print( first_name , last_name)

# print('type of  var: ', type(var) ,'Address: ' ,   id(var))
# print('type of my function ', type(print_name) ,'Address: ' , id(print_name))
# print_name("Gaurav","Rajput")    

# # imperative style 
# def print_name_IMP(first_name,last_name, salutation):
#     print(salutation , end  = ' ' )
#     print_name(first_name, last_name)

# # oops style
# class  my_class():
#     @staticmethod
#     def print_name(first_name,last_name):
#         print( first_name , last_name)

#     @classmethod
#     def print_name_oops(cls,first_name,last_name, salutation):
#         print(salutation , end  = ' ' )
#         cls.print_name(first_name, last_name)

# my_class.print_name_oops("Gaurav","Rajput", 'Mr')        

# # functional style  # print_name_FS is HOF 
# def print_name_FS(rcv_print_function,first_name, last_name, salutation):
#     print(salutation , end = ' ')
#     rcv_print_function(first_name, last_name)
    
    
# print_name_FS(print_name,"Gaurav","Rajput",'Mr')

# # functional style (returned a function as well) # print_name_FS is HOF 
   
# def print_name_FS1(rcv_print_function,salutation):
#     print(salutation , end = ' ')
#     return rcv_print_function
    
    
# ret_val = print_name_FS1(print_name,'Mr')
# ret_val("Gaurav","Rajput")

# # python has some in built methods which are HOF
# def my_custom_sort_val(string_val):
#     if string_val == 'gaurav':
#         ret_val = 1 
#     elif string_val == 'rajput':
#         ret_val = 2 
#     if string_val == 'mr':
#         ret_val = 0 
#     return ret_val     

"""__iterable: Iterable[SupportsRichComparisonT@sorted],
*,
key: None = None,
reverse: bool = False
"""

# print(
# sorted( ['gaurav','rajput','mr'],key = my_custom_sort_val,reverse= False ))

# good to know stuff 
# #That is the python syntax for specifying that
# #every parameter after * must be specified as keyword arguments.
# def func2(__x , *, y, z):
#     print(__x, y, z)

# func2(__x = [100,200,300], y = 200,z = 100 )


# good to know , how can we pass multiple arguments to a function
# simple function that takes in fixed number of arguments
# def func2(x , y, z):
#     print(x, y, z)

# # function that takes in variable number of named arguments
# def func2_d( **x ):
#     for  i in x.values() :
#         print(i , end = ' ')

# # function that takes in variable number of positional arguments
# def func2_t(*x ):
#     for  i in x :
#         print(i , end = ' ')

# # invocations
# func2_t(1,2,3,4)    
# func2_d(x=1,y=2,z=3,a=4)    


# exercise : create my calculator exercise in functional style 
"""
Addition/Squaring/exponenation should be done as part of single function named 
"my_calculator"
which takes in type of operation, number1,number2 as input 
and outputs the answer based on the operation
"""
def hof(func,param1,param2= None):
    return func(param1) if param2 is None else func(param1,param2)
    
#from function_definitions import *
my_addition = lambda first_number,second_number : first_number+second_number
my_square = lambda first_number, second_number = None : first_number**2
my_exponenation = lambda first_number,second_number : first_number**second_number

def my_calculator():
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))

    if choice == 1 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_addition(first_num,second_num)
        returned_value = hof(my_addition,first_num,second_num)
        print("The Addition of the numbers is ",returned_value)

    elif choice == 2 :
        first_num = int(input("Please enter First number:"))
        #returned_value = my_square(first_num)
        returned_value = hof(my_square,first_num)
        print("The Square of the number is ",returned_value)
    elif choice == 3 :
        first_num = int(input("Please enter First number:"))
        second_num = int(input("Please enter Second number:"))
        #returned_value = my_exponenation(first_num,second_num)
        returned_value = hof(my_exponenation,first_num,second_num)
        print("The exponenation of the numbers is ",returned_value)

def iterative_calculator():
    while(True):
        print("Lets start   !!!! ")
        my_calculator()	
        choice = input("\n Do you want to continue (Y/N)").lower()     
        if choice == 'n':
            break

# iterative_calculator() 

# functional style using function object reference and dictionary to navigate to a function runtime
while(True):
    my_invocation_dict = {1: my_addition , 2 : my_square , 3: my_exponenation}
    print("Lets start   !!!! ")
    print("****************** MENU ************************")
    print("1: Addition")
    print("2: Square")
    print("3: Exponentation ")
    choice = int(input ("Please select your choice"))
    
    first_num = int(input("Please enter First number:"))
    if choice !=2 :
        second_num = int(input("Please enter Second number:"))
    
    print('Addition : ' if choice == 1 else 'Square : ' if choice == 2 else 'Exponentation: ' , end = ' ')
    print(my_invocation_dict.get(choice)(first_num,second_num))
    
    choice = input("\n Do you want to continue (Y/N)").lower()     
    if choice == 'n':
        break

    