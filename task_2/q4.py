# Write a program to check if a number is prime.
'''
import math as s
n=int(input("Enter a number : "))
pr=0
if n>2:
    for i in range(2, s.ceil(n**0.5)):
        if n%i==0:
            pr+=1
            break
    if pr==1:
        print("prime hai bhai")
    else:
        print("prime nhi hai bhai")
elif n==1:
    print("prime nhi hai")
else:
    print

'''

n=int(input("Enter a number : "))
if n>2 or n==1:
    if n%2==0 or n%3==0 or n%5==0 or n==1:
        print("not prime")
    else:
        print("prime")
else:
    print("prime")
