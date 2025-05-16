'''WAP to enter marks of 3 subjects from the user and store them in a dictionary.start with the 
empty dictionary and add one by one . use subject names as key and marks as value '''
marks={}
x = int(input("enter the marks of physics: "))
marks.update({"physics":x})
x= int(input("enter the marks of maths: "))
marks.update({"maths":x})
x=int(input("enter the marks of chemistery: "))
marks.update({"chemistery":x})
print(marks)