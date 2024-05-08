#wap to print div of student according to thier result
name=input("Enter the name of student = ")
rollno=int(input("Enter the roll no of student = "))
print("enter the marks of student")
x=int(input("Enter the marks of maths = "))
y=int(input("Enter the marks of english = "))
z=int(input("Enter the marks of science = "))
l=int(input("Enter the marks of hindi = "))
m=int(input("Enter the marks of social = "))
per=(x+y+z+l+m/500)*100
if per>=75:
 print("1st div")
if per>=50 and per<=75:
 print("2nd div")
if per>=33 and per<=50:
 print("3rd div")
if per<=33+:
 print("fail")



 
