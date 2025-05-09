# Print a diamond pattern using stars (*).

n=10
for i in range(1,n+1):
    count=n-i
    print(end=" "*count)
    for j in range(i):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    count=n-i
    print(end=" "*count)
    for j in range(i):
         print("*", end=" ")
    print()