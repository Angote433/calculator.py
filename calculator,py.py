num1 = float(input("Enter the firs number: "))
num2 = float(input("Enter the second number: "))
sign = input("Enter the operator to be used(+,*,/,-): ")

#Operations based on the signs
if sign == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif sign == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif sign == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif sign == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1}  / {num2} = {result}")
    else:
        print("Error! A number cannot be divided by zero")
else:
    print("Invalid operator! Please enter operator to be used(+,*,/,-)")



