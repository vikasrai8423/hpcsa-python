def lucky_student(final_student_list,lucky_student_list):
    is_append = 'N'
    while(is_append == 'N'):
        lucky_student_rollno = final_student_list[ random.randint(1,39)]
        if lucky_student_rollno not in lucky_student_list:
            lucky_student_list.append(lucky_student_rollno)
            print(f"Congratulations {lucky_student_rollno} , Show is all yours !!! ")
            is_append = 'Y'
        
import random
lucky_student_list = []
final_student_list = list(range(1,15) ) + list( range(31,57))

while(True):
    lucky_student(final_student_list,lucky_student_list)
    choice = input("Press Y to exit ").upper()
    if choice == 'Y':
        break