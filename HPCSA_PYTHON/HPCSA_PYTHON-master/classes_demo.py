# template
class Student():
	
    #class variables 
    institute_name = 'CDAC'
    
    # class method
    @classmethod
    def change_institute_name(cls,in_institute_name):
        cls.institute_name = in_institute_name
        
    def __init__(self,in_name,in_rollno,in_subject_enrolled,in_pocket_money):
        # instance variables
        self.name = in_name
        self.rollno = in_rollno
        self._subject_enrolled = in_subject_enrolled # protected variable
        self.__pocket_money = in_pocket_money # private variable 
     
     # instance method
    def display_object_details(self):
         print(f'Name {self.name} Rollno {self.rollno} subject : {self._subject_enrolled} pocket money : {self.__pocket_money}')
    
    # static method
    @staticmethod
    def display_facilities():
        print('I am static method , i do not need any class or object reference (first parameter)')
        
# main method
def main():
    gaurav= Student("Gaurav",1,"Python",100)
    print(type(gaurav))
    gaurav.display_object_details()
    
    sagar= Student("Sagar",2,"Java",200)
    sagar.display_object_details()
    
    print(" Class variable printed ")
    print(f" Before Gaurav's institute: {gaurav.institute_name}")
    print(f"Before Sagar's institute: {sagar.institute_name}")
    Student.change_institute_name("Sunbeam")
    # lets make gaurav go to MIT
    gaurav.institute_name = 'MIT' 
    print(f" After Gaurav's institute: {gaurav.institute_name}")
    print(f"After Sagar's institute: {sagar.institute_name}")
    
    Student.display_facilities()
    gaurav.display_facilities()
    sagar.display_facilities()
    
    # optionally you can access instance variables by using dot notation
    print(f'Name : {gaurav.name}')
    #print(f"Gaurav's pocket money : {gaurav.__pocket_money}")
    # creating a duplicate reference
    gaurav_duplicate = gaurav
    del gaurav # deleting the original reference
    # reference gaurav is cleaned object but object is still in memory since 
    # we have gaurav duplicate pointing to that object
    print(f'Name : {gaurav_duplicate.name}')  
    print(f'Before  : {gaurav_duplicate.institute_name}') 
    del gaurav_duplicate.institute_name # deleting an attribute of the object
    print(f'After  : {gaurav_duplicate.institute_name}') 
      
# executing my main method
# main()
