angle1 = int(input("Enter angle1 : "))
angle2 = int(input("Enter angle2 : "))
angle3 = int(input("Enter angle3 : "))
SumOfAngles = angle1 + angle2  + angle3
if(SumOfAngles == 180):
    print("Triangle is Valid")
else:
    print("Triangle is Invalid")