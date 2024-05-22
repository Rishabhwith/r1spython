'''print the following
value      factorial
----------------------
1             1
2             2
3             6
4             24
5            120 '''
x=int(input("Enter the starting point = "))
y=int(input("Enter the ending point = "))
for i in range(x,y+1):
    factorial=1
    n=x
    for i in range(n,0,-1):
        factorial=factorial*i
    print(i,"\t",factorial)
    
