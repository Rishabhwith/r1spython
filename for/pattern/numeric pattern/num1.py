''' 1
    2 3
    3 4 5
    4 5 6 7'''
n=5
for i in range(1,n):
    val=i
    for j in range(i):
        print(val,end=" ")
        val=val+1
    print()