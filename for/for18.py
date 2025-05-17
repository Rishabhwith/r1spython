'''print the following
0+10=10
1+9=10
2+8=10
.
.10+0=10

'''
x=int(input("Enter the no. 10 = "))
y=int(input("Enter the no. 10 = "))
for i in range(0,x):
    r=i+y
    print(i,"+",y,"=",r)
    y=y-1
