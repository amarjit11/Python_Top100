'''  num=int(input("enter the number "))
if num>0:
	print(num,"is a positive number")
elif num==0:
	print(num,"is zero")
else:
	(num,"is negative number") '''

##### 2nd type
'''
num=int(input("enter the number "))
if num>0:
	if num==0:
		print(num," is zero")
	else:
		print(num, " is positive")
if num<0:
	print(num, "is negative") 
'''
num=int(input("enter the number"))
print("positive" if num>0 else"negative")
