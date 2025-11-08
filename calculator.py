num1 = int(input('enter your number'))
num2 = int(input('enter your number'))

print('Operation: + ,-,/,*')
Operation = input('select your opration')
if Operation == "+":
    result= num1 + num2
elif Operation == "-":
    result= num1 - num2
elif Operation == "/":
    result= num1 / num2
elif Operation == "*":
    result= num1 * num2
    if num2 != 0:
        result = num1 / num2
    else:
        result ="Error"
else:
    result= "invalid operation"
    
print("Result" ,result)

print("hello world")
