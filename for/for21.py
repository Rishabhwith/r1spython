'''sum and avg of even from 1 to x'''
x=int(input("Enter the size = "))
s=0
avg=0
for i in range(1,x+1):
    if(i%2==0):
        print(i)
        s=s+i
        avg=s/x
print("sum of the sequence is the = ",s)
print("avg of the sequence is the = ",avg)
