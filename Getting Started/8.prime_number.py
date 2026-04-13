'''Method 1: Simple iterative solution
Method 2: Optimization by break condition
Method 3: Optimization by n/2 iterations
Method 4: Optimization by √n
Method 5: Optimization by skipping even iteration
Method 6: Basic Recursion technique'''

import math
num=int(input())
flag=0
for i in range(2,num):
	if num%i==0:
		flag=1
	break
if flag==1:
	print(f"{num} is not a prime")
else:
	print(f"{num} is a prime")

# Method 2: Optimization by break condition