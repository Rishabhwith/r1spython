'''  *               *                    
     * *           * *        wap to print the butterfly pattern                                   
     * * *       * * *
     * * * *   * * * *
     * * * * * * * * *
     * * * *   * * * *
     * * *       * * *
     * *           * *
     *               *
                                         '''
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range((n-i-1)*2):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range((i+1)*2):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()