#wap to enter two values and swap them
#b. without using third variable
a=int(input("Enter the 1st value = "))
b=int(input("Enter the 2nd value = "))
print("before swaping the values = ",a,b)
a=a+b
b=a-b
a=a-b
print("after swaping the values = ",a,b)
