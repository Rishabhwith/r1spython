'''sum and avg of even from 1 to x'''
x=int(input("Enter the no. = "))
i=1
s=0
while i<=x:
    if i%2==0:
        print(i)
        s=s+i
        avg=s/x
    i=i+1
print("The sum of even no = ",s)
print("THe avg of even no = ",avg)
        
