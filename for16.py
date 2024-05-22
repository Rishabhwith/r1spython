'''value    square     cube
-----------------------------
1	1	1
2	4	8
.
.
x
'''
x=int(input("Enter the size = "))
print("value\tsquare\tcube")
print("------------------------------------------[")
for i in range(1,x):
    r=i**2
    bir=i**3
    print(i,"\t",r,"\t",bir)
