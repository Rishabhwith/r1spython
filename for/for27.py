'''1.  wap to find armstrong number,perfect number,palindrome in a give range of 1 to 10
   2.  wap to count the number of prime numbers in a given range of 1 to 10'''

n=int(input("enter the range"))
for i in range(1,n+1):
    s=0
    v=int(input())
    temp=v
    while temp>0:
        r=temp%10
        s=s+r**3
        temp=temp//10
    print("armstrong of ",v,"is",s)
    if s==v:
        print(v,"is an armstrong no.")
    else:
        print(v,"is not an armstrong no.")