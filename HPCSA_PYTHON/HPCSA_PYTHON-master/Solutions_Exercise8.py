class Employee:
  # class variable 
  cls_department_name= "CDAC"
  
  def __init__(self,rcv_empid,rcv_emp_salary,rcv_mgr_id):
    # instance variables 
    self.empid= rcv_empid
    self.emp_salary= rcv_emp_salary
    self.mgr_id= rcv_mgr_id
    print(f"{self} was created successfully with values {rcv_empid},{rcv_emp_salary},{rcv_mgr_id}")

  # instance method
  def get_emp_salary(self):
      return self.emp_salary
  
  # instance method
  def set_emp_salary(self,rcv_salary):
      self.emp_salary = rcv_salary

  def display_object(self):
      print(f"Values {self.empid},{self.emp_salary},{self.mgr_id}")

  # class method 
  @classmethod
  def get_department_name(cls):
      return cls.cls_department_name
  
  # static method
  @staticmethod
  def field_expertise():
      print("Some expertise printed here")
  

# 1) create an object employee(100,1000,1)  
my_first_emp_obj = Employee(100,1000,1)

#3) print the department name 
Employee.get_department_name()

#4) display the expertise for the employees
Employee.field_expertise()
my_first_emp_obj.field_expertise()



class My_airline :
    airline_name = 'Gaurav Airline'
    cities = {'Delhi','Pune','Mumbai','Bangalore','Chennai','Hyderabad','Patna','Trivandrum'}
    rows = set(range(1,21))
    section = {'A','B','C','D','E','F'}
    flight_numbers = set(range(564262,564362))
    
    def __init__(self,rcv_fn= None,rcv_dep = None , rcv_arr= None, rcv_sn = None) -> None:
        self.flight_number =  My_airline.flight_numbers.pop()  if rcv_fn is None else rcv_fn
        self.departure = My_airline.cities.pop() if rcv_dep is None else rcv_dep
        self.arrival = My_airline.cities.pop() if rcv_arr is None else rcv_arr
        self.seat_number = str(My_airline.rows.pop()) + My_airline.section.pop() if rcv_sn is None else rcv_sn
        
    def display_details(self):
        print(f"""Your ticket details :
--------------------------------------               
Airline_name : {My_airline.airline_name}
Flight_number : {self.flight_number}
Departure: {self.departure}
Arrival: {self.arrival}
Seat_number: {self.seat_number}
              
              """)   


def main():
   ticket_number1 = My_airline(1111111,'LONDON','USA','XXX1') 
   ticket_number2 = My_airline()
   
   ticket_number1.display_details()
   ticket_number2.display_details()

main()


# var = None
# flight_number =  1  if var else 2   
# print(flight_number)      