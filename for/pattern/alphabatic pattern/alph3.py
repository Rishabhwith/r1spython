''' A B C
    A B C
    A B C'''
n=3
p=65
for i in range(n):
    for j in range(n):
        print(chr(p+j),end=" ")
    print()