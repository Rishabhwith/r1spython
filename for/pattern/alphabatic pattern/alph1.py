''' A B C
    B C D
    C D E '''
P=65
n=3
for i in range(n):
    for j in range(n):
        print(chr(P+i+j),end=" ")
    print()