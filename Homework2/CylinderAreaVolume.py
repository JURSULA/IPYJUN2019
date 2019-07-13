#Compute the Area and Volume of a cylinder by getting radius and length of a cylinder from the user

radius = eval(input("Enter the radius of a cylinder:"))

length = eval(input("Enter the lenght of a cylinder:"))

#Constant

PI = 3.1417

area = PI *(radius**2)

volume = area*length

print("For the given radious:'{0}' and length:'{1}' The area of the cylinder is: {2} and the volume of the cylinder is: {3}".format(radius, length, area, volume))
