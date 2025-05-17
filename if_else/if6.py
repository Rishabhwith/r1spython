'''
enter number of adults and kids gone for a movie and find bill as follows
rate per adult 200
rate per kid 120
if gross bill>15000 then add 28% gst otherwise no gst
'''
adults=int(input("Enter the no. of adults = "))
kids=int(input("Enter the no.of kids = "))
bill = 200*adults+120*kids
if bill>15000:
 gst=(bill*28)/100
else:
 gst=0

totalbill=bill+gst
print("The total bill of movie tickets = ",totalbill)
