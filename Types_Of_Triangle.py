angle1 = int(input("Enter 1st angle of the traingle : "))
angle2 = int(input("Enter 2nd angle of the traingle : "))
angle3 = int(input("Enter 3rd angle of the traingle : "))

# sum of all traingle must be 180 degree
Sum_of_angles = angle1 + angle2 + angle3

# check for right, obtuse and acute traingle
if(Sum_of_angles == 180 and (angle1 == 90 or angle2 == 90 or angle3 == 90)):
    print("This is a Right Angle Traingle...")
elif(Sum_of_angles == 180 and (angle1 > 90 or angle2 > 90 or angle3 > 90)):
    print("This is a Obtuse Traingle...")
elif(Sum_of_angles == 180 and (angle1 < 90 and angle2 < 90 and angle3 < 90)):
    print("This is an Acute Traingle...")
else:
    print("INVALID Traingle")