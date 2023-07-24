# def function_cal(input1, input2):
#     returned_value = input1 + input2
#     print("The Addition of the numbers : ",returned_value)  

# def function_square(input1, input2):
#     returned_value  = input1**2
#     print("The 1st number Square is : " returned value)
    
# def function_expo(input1, input2):
#      returned_value = input1**input2
#      print("The Exponention of the numbers : ",returned_value)  

def function_calculator():

    print ("\n1) Addition\n2) Square of number\n3) Exponantion\n0)Exit")
    choice = int(input("Please enter a choice : "))


    if (choice == 1) :
        input1 = int(input("Enter First number : "))
        input2 = int(input("Enter Second number : "))
        returned_value = input1 + input2
        print("The Addition of the numbers : ",returned_value)  
    
    elif (choice == 2) :
        input1 = int(input("Enter a number : "))
        returned_value = input1**2
        print("The Square of the number is : ",returned_value)  

    elif (choice == 3) :
        input1 = int(input("Enter First number : "))
        input2 = int(input("Enter Second number : "))
        returned_value = input1**input2
        print("The Exponention of the numbers : ",returned_value)  
    
    elif (choice == 0):
        exit
    
    else :
         print("INVALID INPUT")
    
    
choice = 'Y'
while(choice == 'Y' or choice == 'y'):
    function_calculator()
    choice = input("\nDo you want to continue Y/y : ")
    
    



