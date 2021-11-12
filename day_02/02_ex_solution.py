#python program to calculate height of a building
print("Calculate Height of a building using elevation angle")

#get distance from the building
dist=input("Enter the distance from the building")

#get angle of elevation
ang=input("Enter angle of elevation")

#Calculate heiht using tan(ang)*dist=height

import math
height=math.tan(float(ang)*math.pi/180)*float(dist)

print("Height is ", height)
