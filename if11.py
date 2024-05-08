'''
first 500 units @ 2 pu
next 1200 units @ 3pu
next 2000 units @ 4pu
rest @ 5 pu
'''
omr=int(input("Enter the old meter reading = "))
nmr=int(input("Enter the new meter reading = "))
uc=nmr-omr
if uc<=500:
 rate=uc*2
if uc<=1700:
 rate=(500*2)+(uc-500)*3
if uc<=3700:
 rate=(500*2)+(1200*3)+(uc-1700)*4
if uc>3700:
 rate=(500*2)+(1200*3)+(2000*4)+(uc-3700)*5
print("Electricity bill = ",rate)
 
