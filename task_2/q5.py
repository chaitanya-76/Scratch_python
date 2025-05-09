# Print the Fibonacci sequence up to n terms.

n=int(input("Enter a number :"))
a=0
b=1
# print(a,b,end=" ")
for i in range(n):
    print(a, end=" ")
    a,b=b,a+b