'''            print the pyramid
         *
        * *
      * * * *
    * * * * * *
  * * * * * * * * 
* * * * * * * * * *  
'''
n=5
for i in range(n):
    for j in range(i,n-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()


'''n=5    # it is a different way to do print the pyramid pattern
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    if i==0:
        star_count=1 # in this we have used the star count for the 
    else:
        star_count=i*2
    for k in range (star_count):
        print("*",end="")
    print()'''
