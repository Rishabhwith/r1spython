n=int(input("Enter the no. = "))  #  
for i in range (1,n+1):
    v=int(input())#  28
    sum=0  #s=0
    56j=1     #   j=1
    while(j<v): # j= 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
        if v%j==0:    # 28%4==0
            sum+=j   # s=3+4   s=7
        j=j+1
    print("sum of divisor of",v,"is",sum)
    if sum==v:
        print(v,"is a perfect no.")
    else:
        print(v,"is not perfect no.")