## if-else method
'''year= int(input())
if( year%400==0) or (year%4==0 and year%100!=0):
	print("leap year")
else:
	print("not a leap year")'''

#ternary operator
'''year= int(input())
def is_leap(year):
	return True if  (year%4==0 and year%100!=0) or (year%400==0) else False
print(f"{year} is leap year: {is_leap(year)}")'''


#calender module
'''import calendar
year= int(input())
def is_leap_year(year):
	return calendar.isleap(year)
print(f"{year} is a lear: {is_leap_year(year)}")'''

# using lambda function
year= int(input())
is_leap_year= lambda year: True if  (year%4==0 and year%100!=0) or (year%400==0) else False
print(f"{year} is a lear: {is_leap_year(year)}")