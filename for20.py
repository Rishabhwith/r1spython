'''sum and avg of sequence frm 1 to 20'''
s=0
avg=0
x=int(input("Enter the size = "))
for i in range(1,x+1):
    s=s+i
    avg=s/x
    print(i)
print("Sum of the sequence is = ",s)
print("Avg of the sequence is = ",avg)
    
