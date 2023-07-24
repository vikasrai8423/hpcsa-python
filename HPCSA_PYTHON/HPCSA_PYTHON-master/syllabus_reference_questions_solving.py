# #  Using for loop, write and run a Python program for this algorithm.
# # 10 Factorial = 10*9*8*7*6*5*4*3*2*1

# fact = 1
# for i in range(int(input('Enter number: ')),1,-1):
#     fact*= i
# print(fact)    

# #.2. Modify the program above using a while loop so it prints out all of the factorial values that are 
# # less than 2 billion. (You should be able to do this without looking at the output of the previous 
# # exercise.)


# fact = 1
# input_num = int(input("Please enter number: "))
# cnt = input_num
# while ( cnt > 1 ):
#     fact = fact*cnt 
#     cnt = cnt-1

# if fact < 2000000 :
#     print(fact)    
# else:
#     print("Sorry limit excedded of 2 Billion ")    

# input_number_of_days = int(input("Days: "))
# start_day_of_week = int(input('0: Monday 1 : Tuesday ... '))
# print(f'S  M  T  W  T  F  S')
# cnt = 1
# for i in range((start_day_of_week-1)*-1, input_number_of_days+1,1):
#     print(f'{i:2}' if i > 0 else ' ' , end= ' ')
#     if cnt%7 == 0 :
#         print('')
#     cnt = cnt+1    

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 
'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 
'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 
'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', ' ': ' '}

secret_message = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'
for i in secret_message:
    print( key.get(i) , end = '')
    
    