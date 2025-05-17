'''value    square     cube
-----------------------------
1	1	1
2	4	8
.
.
x
'''
x=int(input("Enter the no. = "))
i=1
print("value\tsquare\tcube")
print("---------------------------------------")
while i<=x:
    result=i**2
    bit=i**3
    print(i,"\t",result,"\t",bit)
    i=i+1
