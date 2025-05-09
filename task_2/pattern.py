# print right angle triangle
'''n=5
for i in range(5):
    print('*'*(i+1))'''

# print inverted
'''n=5
for i in range(5):
    print('*'*(n-i))'''

# triangle started from spaces
'''n=5
for i in range(1,n+1):
    print(" "*(n-i), '*'*i)'''

# triangle end from spaces
'''n=5
for i in range(n+1):
    print(" "*i, '*'*(n-i))'''

# using nested loop
'''
n=5
for i in range(n):
    for j in range(i):
        print('*', end="")
    print("*")

'''

# square
'''
for i in range(1,6):
    for j in range(1,6):
        print("*", end=" ")
    print()'''

# triangle
'''
for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()
'''

# inverted triangle
'''
for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
'''

# number triangle
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
'''

