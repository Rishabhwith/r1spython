n=int(input("Eneter the range"))
for i in range (1,n+1):
    v=int(input())
    s=0
    temp=v
    while(temp>0):
        r=temp%10
        s=(s*10)+r
        temp=temp//10
    print("reverse of",v,"is",s)
    if s==v:
        print(v,"is a palindrome")
    else:
        print(v,"is not a palindrome")