#TASK 1:

# agestr, driverslicence=input("How old are you? Do you have a drivers licence?"). split()
# age=int(agestr)
#
# result = age>18 and driverslicence=="Yes"
#
# print ("You are able to drive :" + str(result))

# TASK 2:

# password=input("What is your password?")
# a=len(password)
# result= (a>=8)
#
# print("Password accepted :" + str(result))

# TASK 3:

# astr,bstr = input ("Enter 2 digits"). split()
# a=int(astr)
# b=int(bstr)
#
# result = ((a % 2)==0) and ((b % 2)==0)
# result1 = ((a % 2)==0) or ((b % 2)==0)
# print("Both numbers are even: " + str(result))
# print("At least one number is even: " + str(result1))

# TASK 4:

# yearstr=input("Enter a year")
# year=int(yearstr)
# leapyear=((year % 4) == 0) or ((year % 400) == 0) and ((year % 100)!= 0)
#
# print ("Leap year: " + str(leapyear))

# TASK 5:
day, month, year=input("Enter the date: day, month, year"). split()
currentyear=2023

a = int(day)<=31
b = int(month)<=12
c = int(year) <= currentyear

datevalid= a and b and c
print("Date valid: " + str(datevalid))

