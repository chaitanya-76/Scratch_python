# create a calculator that supports +, -, *, / using conditionals. 
a,b = map(int, input("Enter operants : ").split())
op = input("Enter operator (+,-,*,/) : ")
if op=='+':
    print("Addition is ", a+b)
elif op=='-':
    print("Subtraction is ", a-b)
elif op=='*':
    print("Multiplication is ", a*b)
else:
    if b==0:
        print("not divisible")
    else:
        print("Division is ", a/b)