'''print the following
0+10=10
1+9=10
2+8=10
.
.10+0=10

'''
x=int(input("Enter the no. 10 = "))
y=int(input("Enter the no. 10 = "))
i=0
while i<=x:
    l=i+y
    print(i,"+",y,"=",l)
    i=i+1
    y=y-1
