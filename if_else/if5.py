'''
enter qty and rate and print payable amt as follows
if qty>12000 then dis 10% otherwise 5%

'''
qty=int(input("Enter the quantity = "))
rate=int(input("Enter the rate = "))
bill=qty*rate
if qty>12000:
 discount=bill*(10/100)
else:
 discount=bill*(5/100)

total=bill-discount
print("The total bill of costomer = ",total)
