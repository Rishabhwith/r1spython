from math import inf
n=int(input("Enter the range = "))
max=-inf
min=inf
print("Enter the no. = ")
for i in range(1,n+1):
    v=int(input())
    sum=0
    temp=v
    while(temp>0):
        r=temp%10
        sum=(sum*10)+r
        temp=temp//10
    print("reverse of no. ",v,"is",sum)
    if sum>max:
        max=sum
    if sum<min:
        min=sum
print("maximum no. is ",max)
print("minimum no. is ",min)
print("difference of max & min no. of revese is ",max-min)