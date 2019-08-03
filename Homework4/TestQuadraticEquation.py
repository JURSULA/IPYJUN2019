from QuadraticEquation import QuadraticEquation

a = int(input(print("Enter the first coefficient:")))
b = int(input(print("Enter the second coefficient:")))
c = int(input(print("Enter the third coefficient:")))

quadraticequation = QuadraticEquation(a,b,c)
#quadraticequation = QuadraticEquation(5,4,5)
quadraticequation.getDiscriminant()


