A = int(input("Enter a no. : "))
# check divisibilty by 5 and 11
if(A % 5 == 0 and A % 11 == 0):
    print("Number",A,"is Divisible by Both 5 and 11")
elif(A % 5 == 0 or A % 11 == 0):
    print("Number",A,"is EITHER Divisible by 5 OR 11")
else:
    print("Number",A,"is NEITHER Divisible by 5 NOR 11")