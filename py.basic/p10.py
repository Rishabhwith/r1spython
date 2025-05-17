#calculate amt rate year
p,r,t=2100,4.5,5
si=(p*r*t)/100
amt=p*(1+(r/100))**t
ci=amt-p
print("simple interest = ",si)
print("compount interest = ",ci)
