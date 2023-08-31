num1 = input ("This is your 1st number: ")
num2 = input ("This is your 2nd number: ")
a = int(num1)
b = int(num2)
operator = input("Choose an operator (+, -, *, /, %):")
if operator == "+":
 result = a + b
 print (str(a) + " + " + str(b) + " = " + str(result))
elif operator == "-":
 result = a - b
 print (str(a) + " - " + str(b) + " = " + str(result))
elif operator == "*":
 result = a * b
 print (str(a) + " * " + str(b) + " = " + str(result))
elif operator == "/":
 result = a / b
 print (str(a) + " / " + str(b) + " = " + str(result))
elif operator == "%":
 result = a % b
 print (str(a) + " % " + str(b) + " = " + str(result))
else:
 print ("Input Invalid")
