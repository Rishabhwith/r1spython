#wap to enter number of adults and kdis gone for a movie and find bill
#as follows
#rate per adutl 200
#rate per kdi 230
#add 28% gst also to the bill
adults=int(input("enter the no. of adults = "))
kids=int(input("enter the no. of kids = "))
bill=200*adults+230*kids
gstamount=(bill*(28/100))/100
totalbill=bill+gstamount
print("The total bill of costomer including gst= ",totalbill)
