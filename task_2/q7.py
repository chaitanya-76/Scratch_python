# Count how many digits a number has without converting to string. 

n=int(input("Enter a number : "))
sum=0
while n!=0:
    n=n//10
    sum+=1
print(sum)