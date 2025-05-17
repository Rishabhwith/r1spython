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
i=1
print("value\tpower\tresult")
print("------------------------------")
while i<=x:
    result=i**y
    print(i,"\t",y,"\t",result)
    i=i+1
    y=y+1
    
