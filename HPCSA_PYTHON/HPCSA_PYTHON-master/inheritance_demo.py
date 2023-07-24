from  classes_demo import Student
class HPCSA_student(Student):
    
    def __init__(self,in_name,in_rollno,in_pm,in_subject,in_alternate_skills):
        super().__init__(in_name,in_rollno,in_pm,in_subject)
        self.alternate_skills = in_alternate_skills
        
    # I overrided the method since the signature(name+input_paramater) is the same as that of parent
    def display_object_details(self):
        super().display_object_details()
        print(f' Alternate_skills : {self.alternate_skills}')
     
    def add_alternate_skill(self,rcv_alternate_skill):
        self.alternate_skills.append(rcv_alternate_skill)
    
    # overloading support absent in python
    def add_alternate_skill(self,rcv_alternate_skill,proficency_level):
        self.alternate_skills.append(rcv_alternate_skill +'P-->' + proficency_level )
            
pratik = HPCSA_student('Pratik',1,'Python',100, ['Java','C++'])
pratik.display_object_details()
pratik.add_alternate_skill('Hadoop','Expert')
pratik.display_object_details()