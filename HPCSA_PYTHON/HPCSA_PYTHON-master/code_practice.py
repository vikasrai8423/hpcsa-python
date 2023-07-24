# #Given a list, write a Python program to swap first and last element of the list.
# # Input : [12, 35, 9, 56, 24]
# # Output : [24, 35, 9, 56, 12]

# # inp1= input("Please enter the first list of numbers comma seperated ").split(',')
# # print(inp1)
# # # converting the list of strings inot list of integers
# # for i in range(0,len(inp1),1):
# #     inp1[i] = int(inp1[i])
# # print(inp1)
# # # swap logic 
# # # swap_var = inp1[-1:-2:-1]
# # # inp1[-1:-2:-1] = inp1[0:1:1]
# # # inp1[0:1:1] = swap_var

# # inp1[0:1:1] ,inp1[-1:-2:-1] = inp1[-1:-2:-1] ,inp1[0:1:1]
# # print(inp1)

# # #Given a list, find maximum in the list 
# # inp1= input("Please enter the first list of numbers comma seperated ").split(',')
# # print(inp1)

# # # converting the list of strings inot list of integers
# # for i in range(0,len(inp1),1):
# #     inp1[i] = int(inp1[i])
# # print(inp1)

# # my_max= 0 
# # my_min = 99999999
# # my_cnt = 0 
# # my_sum = 0 

# # for i in inp1:
# #     if my_max < i :
# #         my_max = i 
# #     if my_min > i :
# #         my_min = i         
# #     my_sum +=i
# #     my_cnt +=1

# # print(f"Maximum : {my_max} , Minimum : {my_min} , Count : {my_cnt} , Sum :  {my_sum}")
# # print(f"Maximum : {max(inp1)} , Minimum : {min(inp1)} , Count : {len(inp1)} , Sum :  {sum(inp1)}")


# # 
# # Reverse a list in python 
# inp1= input("Please enter the first list of numbers comma seperated ").split(',')
# print(inp1)

# # converting the list of strings inot list of integers
# for i in range(0,len(inp1),1):
#     inp1[i] = int(inp1[i])
# print(inp1)

# inp1.reverse()
# print('Reversed using inbuilt function ', inp1 )

# inp1 = inp1[-1:(len(inp1)+1)*-1:-1]
# inp1 = inp1[::-1]
# print('Reversed using slicing ', inp1 )

# # concontenate 2 lists 
# list1 =  input("Enter comma separated list values ").split(',')
# list2 =  input("Enter comma separated list values ").split(',')
# list3= []
# for i in range(0,len(list1)):
#     list3.append(list1[i] + list2[i])

# print(list3)    

# #Exercise 3: Turn every item of a list into its square
# numbers = [1, 2, 3, 4, 5, 6, 7]

# for i in range(0,len(numbers)):
#     numbers[i] = numbers[i]*numbers[i]

# print(numbers)    

#Exercise 5: Iterate both lists simultaneously
#Given a two Python list. 
# Write a program to iterate both lists simultaneously 
# and display items from list1 in original order 
# and items from list2 in reverse order.

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]

# for i in range(0,len(list1)):
#     print(list1[i] , list2[len(list2)-i-1])
    

#Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for val in list1:
#     if val == "" :
#         list1.remove(val)

# i = 0 
# while ( i < len(list1)):
#     if list1[i] == "" :
#         del list1[i]
#     i+=1    
    
# print(list1)
    
# # val1 = ""
# # val2 = ""

# # print(id(val1) , id(val2))

    
# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 
# in the following Python List

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]    
# list1[2][2].append(7000)
# print(list1)

# Exercise 9: Replace list’s item with new value if found
# You have given a Python list.
# Write a program to find value 20 in the list, 
# and if it is present, replace it with 200.
# Only update the first occurrence of an item.

# list1 = [5, 10, 15, 20, 25, 50, 20]
# list1[list1.index(20)] = 200
# print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# list1 = [5, 20, 15, 20, 25, 50, 20]
# for i in range(list1.count(20)):
#     list1[list1.index(20)] = 200

# print(list1)    




# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

# temp_list = []
# for i in range(len(keys)):    
#     temp_list.append((keys[i],values[i]))
# answer_dict=  dict(temp_list)
# print(answer_dict)

# answer_dict = {}
# for i in range(len(keys)):
#     answer_dict[keys[i]] = values[i]
# print(answer_dict)        

# # Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# # Expected output:

# # {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict1.update(dict2)
# print(dict1)

print("geGE".lower().count('ge'))