# wap to print largest of three
x=int(input("Enter the 1st no. = "))
y=int(input("Enter the 2nd no. = "))
z=int(input("Enter the 3rd no. = "))
if x>y:
    if x>z:
        print("largest is = ",x)
    else:
        print("largest is = ",z)
else:
    if y>z:
        print("largest is = ",y)
    else:
        print("largest is = ",z)
