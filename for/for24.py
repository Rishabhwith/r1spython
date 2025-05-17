'enter x values and print their sum and avg'
x=int(input("Enter the starting value = "))
y=int(input("Enter the ending value = "))
s=0
for i in range(x,y+1):
    v=int(input("Enter the value = "))
    s=s+v
avg=s/y
print("sum of the values = ",s)
print("avg of the values = ",avg)
