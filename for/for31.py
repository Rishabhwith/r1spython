#wap to print difference between max and min from the digit ex 6578  8-5=3
from math import inf
max=-inf
min=inf
for i in range(1,2):
    v=int(input())
    temp=v
    while(temp>0):
        r=temp%10
        if(r>max):
            max=r
        if(r<min):
            min=r
        temp=temp//10
print(max)
print(min)
print("Diffrence between digits = ",max-min)