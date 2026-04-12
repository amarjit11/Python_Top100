'''num1=int(input("enter the smaller number: "))
num2=int(input("enter the bigger number: "))

if num1>num2:
	print(num1)
else:
	num2 '''

## using ternary
num1=int(input("enter the smaller number: "))
num2=int(input("enter the bigger number: "))
print((num1 if num1>num2 else num2))