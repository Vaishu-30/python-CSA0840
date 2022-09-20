year = int (input ("Enter a year:"))

# Determine if it is a leap year
if  year %  400  == 0:
   isLeapYear   = True
elif year % 100 == 0:
   isLeapYear   = False
elif year % 4  == 0:
   isLeapYear   = True
else :
   isLeapYear   = False

# Display the result
if isLeapYear:
   print (year, "is a leap year.")
else :
   print (year, "is not a leap year.")

