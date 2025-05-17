'''enter x values and print their sum and avg'''
i=int(input("enter the statring value = "))
s=0
avg=0
x=int(input("Enter the size = "))
while i<=x:
    v=int(input("Enter the value = "))
    s=s+v
    i=i+1
avg=s/v
print("THe sum of the values = ",s)
print("The average of the values = ",avg)
