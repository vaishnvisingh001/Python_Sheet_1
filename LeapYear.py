# Input a Year
year = int(input("Enter a Year: "))

# Check if it's a leap year
if (year % 400 == 0):
    print(year, "is a Century Leap Year")
elif (year % 100 == 0):
    print(year, "is a Century Year but NOT a Leap Year")
elif (year % 4 == 0):
    print(year, "is a Non-Century Leap Year")
else:
    print(year, "is NOT a Leap Year")