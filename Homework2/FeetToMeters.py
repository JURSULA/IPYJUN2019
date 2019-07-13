#Convert Feet into Meters by getting the Feet input from the user

feet = eval(input("Enter the Value in feet:"))

#constant

METERS_PER_FOOT = 0.305

meters = METERS_PER_FOOT * feet

print("{0} feet is {1} meters".format(feet, meters))
