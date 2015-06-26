import math
balance = 320000
annualInterestRate = 0.2
monthlyRate = annualInterestRate/12
c = monthlyRate+1

emi =  ((1-c)*balance*math.pow(c,12)) /(1- math.pow(c,12))
print emi

print 'Lowest Paym1ent: '+str(emi)