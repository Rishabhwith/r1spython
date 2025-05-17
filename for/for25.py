'find factorial of x'
x=int(input("Enter the value = "))
factorial=1
for i in range(x,0,-1):
    factorial=factorial*i
    print(i,"*",end="\t")
print("Facorial is =",factorial)
