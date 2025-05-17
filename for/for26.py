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
print("value\tfactorial")
for i in range(x,y+1):
    factorial=1
    for j in range(i,0,-1):
        factorial=factorial*j
    print(i,"\t",factorial)
    
