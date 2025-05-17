'''print the following
value      factorial
----------------------
1             1
2             2
3             6
4             24
5            120 '''
x=int(input("Enter the starting point = "))
n=int(input("Enter the ending point = "))
print("VALUE\tFACTORIAL")
print("-----------------------------")
while x<=n:
    factorial=1
    y=x
    while y>0:
        factorial=factorial*y
        y=y-1
    print(x,"\t",factorial)    
    x=x+1

