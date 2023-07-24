module_scope_variable = 10 
temperature_today = 40

def my_function(input_var):
    function_scope_variable = 20
    temperature_today = 50
    print('Value inside of function is ' , function_scope_variable )
    print('Value inside of function for temperature_today: ' , temperature_today )
    print(module_scope_variable)


print(module_scope_variable)
print('Value Outside of function for temperature_today: ' , temperature_today )
# print(function_scope_variable) # error 
# print(input_var)

my_function("Passed_value_to_function")

for i in range(10):
    pass

print('outside of loop i is ' , i)    