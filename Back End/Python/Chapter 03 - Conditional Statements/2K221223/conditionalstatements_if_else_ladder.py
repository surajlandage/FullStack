# Conditional Statements

# 1. Decision Making

# controle statement - if-else ladder

# Ex. To find largest of 3 numbers

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if (num1 > num2 and num1 > num3):
    print(num1, "is greater than", num2, "and", num3)
elif (num2 > num1 and num2 > num3):
    print(num2,"is greater than", num1, "and", num3)
else:
    print(num3, "is greater than", num1, "and", num2)

