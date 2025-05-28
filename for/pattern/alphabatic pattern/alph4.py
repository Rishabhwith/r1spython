'''A B C 
   D E F
   G H I'''
n=3
p=65
for i in range(n):
    for j in range(n):
        print(chr(p),end=" ")
        p=p+1
    print()