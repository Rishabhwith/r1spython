'''
value   power  	result
x          1       ?
x           2      ?
.
.
x         y        ?

'''
x=int(input("Enter the size = "))
y=int(input("Enter the power = "))
for i in range(1,x):
    r=i**y
    print(i,"\t",y,"\t",r)
    y=y+1
