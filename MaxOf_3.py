num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
num3 = int(input("enter num3 : "))
# maximum among 3
if (num1 > num2 and num1 > num3):
    print("num 1 =",num1,"is Maximum of all.")
elif(num2 > num3):
        print("num2 =",num2,"is Maximum of all")
else:
    print("num3 =",num3,"is Maximum of all")