'''Financial application to calcualte tips and grand total in a bill by
getting subtotal and gratuity rate from user'''

subTotal = eval(input("Enter the subtotal:"))
gratuityPercentage = eval(input("Enter the gratuity rate:"))

#Computer Gratuity Rate

gratuityRate = subTotal *(gratuityPercentage/100)

#Computer Grand Total

grandTotal = gratuityRate + subTotal

print("The Gratuity is {0} and the Grand Total is {1}".format(gratuityRate, grandTotal))





