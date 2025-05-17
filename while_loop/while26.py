'find factorial of x'
x=int(input("ENter the no.= "))
factorial=1
while x>0:
    factorial=factorial*x
    print(x,"*",end="\t")
    x=x-1
print("Factorial is:",factorial)
