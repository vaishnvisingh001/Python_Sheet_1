num = int(input("Enter a no. : "))
# check divisibilty by 3 & lastDigit 4 
if(num % 3 == 0 and num % 10 == 4):
    print(num,"is Divisible by 3 and last digit is 4 ")
elif(num % 3 == 0 or num % 10 == 4):
    print(num,"is EITHER Divisible by 3 OR last digit is 4 ")
else:
    print(num,"is NEITHER Divisible by 3 NOR last digit is 4 ")