
def my_addition(first_num,second_num):
    return first_num+ second_num


def my_square(first_num):
    return first_num**2

def my_exponenation(first_num,second_num):
    return first_num**second_num


def my_uppercase_func(received_string):
    return received_string.upper()


def raise_sal_percent(existing_salary,raise_salary_percentage):
    return existing_salary + (existing_salary*raise_salary_percentage/100) 
    
def get_height(height):
    return round((height/30.48),2)
    

def convert_to_rupee(no_of_dollars):
    return no_of_dollars*82

def get_fare_details(source, destination, fare_in_INR, discount_rate_percentage):
    return "Fare from" + source +" to " + destination + " is " + str(fare_in_INR- (fare_in_INR*discount_rate_percentage/100) ) + " INR with has a applied discount of " + str(discount_rate_percentage)+ "%"

