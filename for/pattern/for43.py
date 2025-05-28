''' *   wap to print left pascle triangle
    * *
    * * *
    * * * *
    * * * * *
    * * * *
    * * *
    * * 
    * 
'''
n=5
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()