def fuzz_buzz():
	input_num = int(input("please enter a number"))

	remainder_from_3 = input_num%3
	remainder_from_5 = input_num%5

	if remainder_from_3==0 and remainder_from_5 ==0 : 
			print(" Fizz Buzz")
	elif remainder_from_3 == 0 :
		print("Fizz")
	elif remainder_from_5 == 0 :
		print("Buzz")




choice = 'Y'
while(choice == 'Y' or choice == 'y'):
     fuzz_buzz()
     choice = input("Do you want to continue , Press anything other than Y/y to exit ")

	
 
 
 