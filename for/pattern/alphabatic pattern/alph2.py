''' A A A
    B B B
    C C C'''
n=3
p=65
for i in range(n):
    for j in range(n):
        print(chr(p+i),end=" ")
    print()
