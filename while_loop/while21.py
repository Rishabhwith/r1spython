'''sum and avg of sequence frm 1 to 20'''
x=int(input("Enter the no. = "))
i=1
s=0
avg=0
while i<=x:
    print(i)
    s=s+i
    avg=s/x
    i=i+1
print("sum of the sequence is = ",s)
print("average of the sequence is = ",avg)

