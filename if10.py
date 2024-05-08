''' enter old meter reading and new meter reading and find electricity bill as follows
uc = nmr-omr

uc<1000 then rate 2 pu
otherwise 3 pu
'''
omr=int(input("Enter the old meter reading = "))
nmr=int(input("Enter the new meter reading = "))
uc=nmr-omr
if uc<=1000:
 rate=uc*2
else:
 rate=(1000*2)+(uc-1000)*3
print("Electricity bill = ",rate)


'''
# first 1000 units @ 2pu
rest 3 pu
'''


'''
first 500 units @ 2 pu
next 1200 units @ 3pu
next 2000 units @ 4pu
rest @ 5 pu
'''
