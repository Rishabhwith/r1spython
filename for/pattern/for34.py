''' wap to print the right downward triangle pattern.
    * * * * * 
    * * *
    * *
    *        '''
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()