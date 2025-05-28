count=0
for i in range(1,1001):
    temp=i
    sum=0 
    c=0
    while(temp>0):
            r=temp%10
            sum=(sum*10)+r
            temp=temp//10
            c=c+1
    if i==sum and c==2:
      print(i)
      count=count+1
print("The count of two digit palindrome no. are = ",count)