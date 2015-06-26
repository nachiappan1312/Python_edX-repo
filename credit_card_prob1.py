balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyinterestrate = annualInterestRate/12
tot_paid = 0
for i in range(1,13):
    print "Month: " + str(i)
    Min_Month_Payment = balance*monthlyPaymentRate
    tot_paid += Min_Month_Payment    
    print 'Minimum monthly payment: ' +str(round(Min_Month_Payment,2))
    balance = balance - Min_Month_Payment
    balance = (1+monthlyinterestrate)*balance
    print 'Remaining balance: ' + str(round(balance,2))

print 'Total paid: ' + str(round(tot_paid,2))
print 'Remaining balance: '+str(round(balance,2))
