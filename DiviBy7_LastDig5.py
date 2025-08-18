num = int(input("Enter a no. : "))
# check divisibilty by 7 & lastDigit 5
if(num % 7 == 0 and num % 10 == 5):
    print(num,"is Divisible by 7 and last digit is 5 ")
elif(num % 7 == 0 or num % 10 == 5):
    print(num,"is EITHER Divisible by 7 OR last digit is 5 ")
else:
    print(num,"is NEITHER Divisible by 7 NOR last digit is 5 ")