#Buiding a Calculator

number1 = float(input("Enter the first number:"))
operator = input("Enter an operator:")
number2 = float(input("Enter the second number:"))

if operator == "+":
    print(number1 + number2)

elif operator == "-":
    print(number1 - number2)

elif operator == "*":
    print(number1 * number2)

elif operator == ("/"):
    print(number1 / number2)

elif operator == ("%"):
    print(number1 % number2)

else:
    print("The Operator is Invalid!")
