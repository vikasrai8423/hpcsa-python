# exceptions link for reference
# https://docs.python.org/3/library/exceptions.html

class i_dont_like_value_10_exception(Exception):
    pass

def division( num1,num2):
    try:    
        # ude
        if num1==10 or num2==10:
            #raise i_dont_like_value_10_exception("My own exception")
            raise ZeroDivisionError
        
        return num1//num2
    except ZeroDivisionError:
        print("Internal code --- > Divisor cannot be zero!!!")
    except Exception:    
        print("I dont know what the exception type is but this is a generic exception")
    finally :
        print("This is finally block ")
        
def my_cal():
        print(division(100,10))
my_cal()    


