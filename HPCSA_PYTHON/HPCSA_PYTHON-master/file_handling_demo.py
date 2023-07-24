
# ------------
# File handling
# -------------

# # Python program to demonstrate  opening a file
# file1 = open('my_first_file.txt','rt')
# print(file1.read())
# print("Before closing explicitly" , file1.closed)  
# file1.close()
# print("After closing explicitly" , file1.closed)  

# # no need to close if we use with context
# print("Read call below \n -----------------------")

# with( open('my_first_file.txt',"r") as file1):
#     print("Before coming out of with block " , file1.closed)   
#     print(file1.read())
# print("After coming out of with block " , file1.closed)   

# print("Readline call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readline(),end= "---\n")

# print("Readlines call below \n -----------------------")
# with( open('my_first_file.txt',"r") as file1):
#     print(file1.readlines(),end= "---\n")


# print(r" strip off those \n at the end of the list ")
# with ( open('my_first_file.txt',"r") )as file1:
#     lines = []
#     for line in file1:
#         lines.append(line.strip())
# print(lines)        

# print(" Write to a file in w mode ")
# with ( open('my_first_file.txt',"w") as file1):
#     file1.write("hi there \nhow are you doing ")

# print(" Write to a file in a mode ")
# with ( open('my_first_file.txt',"a") as file1):
#     file1.write("hi there ")

# # read is the primary functionality write is just added as secondary
# with( open('my_first_file.txt',"r+") as file1):
#     print(file1.read())
#     file1.write("I am writing")
  
# # write is primary read is secondary functionality
# with( open('my_first_file.txt',"w+") as file1):
#     print(file1.read())
#     file1.write("hello")

# # append is the primary objective , read functionality is added
# with( open('my_first_file.txt',"a+") as file1):
#     file1.write("append+")
#     file1.seek(7)
#     print(file1.read())


# # Python program to demonstrate  opening a file in binary mode
# file1 = open('my_first_file.txt',"rb")
# print(file1.read())
# file1.close()

# # Python program to demonstrate  writing a file in binary mode
# file1 = open('my_first_file.txt',"wb")
# file1.write(b'0000000000000000000000000000000000000000000')
# file1.close()

# Python program to demonstrate  that the mode in which you open
# the file is read in that way ireespective of which mode it
# was written (earlier  0 was written in binary but read in text back)
# file1 = open('my_first_file.txt',"a+")
# file1.write('111111111111111111111111111111111111')
# file1.seek(0)
# print(file1.read())
# file1.close()

# """
# # Key takeaways
# 1) Open / close / read / write
# 2) open modes ( r,w,a,x,r+,w+,a+)
# 3) text / binary format
# """
# #lets you know if the file handle is closed or not 
# print(file1.closed)

# # Python program to demonstrate  opening a file with some exception handling
# try:
#     file1 = open('my_first_file.txt',"r")
#     print("I am reading the existing file -->\n", file1.read())
# except FileNotFoundError:
#     print("File Not present , I am goind ahead and creating a file for you with some default text !!! ")    
#     file1 = open('my_first_file.txt',"w+")
#     file1.write("Default creation was done in exception block")
#     # file1.writelines(['first_line\n','second_line\n','third_line'])
    
#     print("I am location ", file1.tell())
#     print("I am resetting it at 0 " , file1.seek(0))
#     print("I am location after resetting ", file1.tell())
#     print("I am reading just after writing-->", file1.read())
#     file1.close()

# # program to read from one file and write to another file 
# output_file= open('my_first_file_output.txt','w+')
# for input_line in open('my_first_file.txt'):
#     output_file.write('HPCSA'+input_line)

# output_file.seek(0)    
# print(output_file.read())


# program to read from one file and write to the same file 
input_file = open('my_first_file.txt')
temp_data = input_file.readlines()
input_file.close()

output_file= open('my_first_file.txt','w+')
for input_line in temp_data:
    output_file.write('HPCSA'+input_line)

output_file.seek(0)    
print(output_file.read())

# program where we are using os module along with file handling
import os 

current_file_abs_path = __file__ # gives absolute path of the file 
current_directory = os.getcwd() # gives current working directory path 
target_folder_path = os.path.join(current_directory,'output') # creates path from strings

if 'output' not in os.listdir(current_directory): # gets all files folders in list
     os.mkdir(target_folder_path) # creates a folder

target_path = os.path.join(target_folder_path,'my_first_file_output.txt')

# output_file= open('C:\\Users\\acer\\Desktop\\HPCSA_python\\output\\my_first_file_output.txt','w+')
output_file= open(target_path,'w+') # we use the variable instead of harcoded value
for input_line in open('my_first_file.txt'):
    output_file.write('HPCSA'+input_line)

output_file.seek(0)    
print(output_file.read())    