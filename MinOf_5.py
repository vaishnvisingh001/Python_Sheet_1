num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))
num3 = int(input("enter num3 : "))
# minimum among 3
if (num1 < num2 and num1 < num3):
    print("num1 =",num1,"is Minimum of all.")
elif(num2 < num3):
        print("num2 =",num2,"is Minimum of all")
else:
    print("num3 =",num3,"is Minimum of all")