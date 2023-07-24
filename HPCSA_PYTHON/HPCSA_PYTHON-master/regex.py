"""
--------------------------------
Exercises -- Regular Expressions
-------------------------------
Given the list of strings as input :

gaurav1234@gmail.com
pratik190900234@gmail.com
2009_rocking_person@yahoo.com
GodFather2022@yahoo.com
Brocklesner_89_WWE@yahoo.com
TheRock_WWE@yahoo.com
JohnCena_WWE@yahoo.com
Undertaker_Roman_reigns@outlook.com
6789764666@rediffmail.com
Kane#6789@gmail.com


1) provide me the list of emails that do have special characters of #~`!
2) provide me the list of emails that start with numbers
3) provide me the list of emails that start with numbers followed by an underscore
4) provide me the list of emails that start with numbers followed by an underscore or small case characters
5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
6) Provide me list of emails with only numbers before the @
7) Provide me list of emails with numbers anywhere before the @

"""




import re

l1 = ["2009_rocking_person@yahoo.com",
       "GodFather2022@yahoo.com",
        "Brocklesner_89_WWE@yahoo.com",
        "TheRock_WWE@yahoo.com" ,
        "JohnCena_WWE@yahoo.com" ,
        "Undertaker_Roman_reigns@outlook.com" ,
        "6789764666@rediffmail.com" ,
        "Kane#6789@gmail.com"]



for elem in my_list:
    test_string = elem
    result = re.search(".*[#~`!].*", test_string)  
    if result:
        print("Email Id :" , result.group(0))
        
        
print(l1[0])

#1) provide me the list of emails that do have special characters of #~`!
for i in range(len(l1)):
    str=l1[i]
    a=re.search(".*[#~`!].*",str)
print(a)

#2) provide me the list of emails that start with numbers
for i in range(len(l1)):
    str=l1[i]
    a=re.search("^[0-9].*[a-z].*[@].*",str)
print(a)


#3) provide me the list of emails that start with numbers followed by an underscore
for i in range(len(l1)):
    str=l1[i]
    a=re.search("^\d+_.*[@].*",str)
print(a)

#4) provide me the list of emails that start with numbers followed by an underscore or small case characters
for i in range(len(l1)):
    str=l1[i]
    a=re.search("^[0-9]+[_a-z].*[@].*",str)
print(a)

#5) provide me the list of emails that start with numbers followed by an underscore or small case characters or large case characters
for i in range(len(l1)):
    str=l1[i]
    a=re.search("^[0-9]+[_a-zA-Z].*[@].*",str)
print(a)

#6) Provide me list of emails with only numbers before the @
for i in range(len(l1)):
    str=l1[i]
    a=re.search("^[0-9]+[@].*",str)
print(a)

#7) Provide me list of emails with numbers anywhere before the @
for i in range(len(l1)):
    str=l1[i]
    a=re.search("^.*\d+[@].*",str)
print(a)


#  if a:
#         print("Email Id :" , result.group(0))