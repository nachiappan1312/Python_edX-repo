import math
balance = 320000
annualInterestRate = 0.2
lower_limit = balance/12
mon_payment = lower_limit
mon_int = annualInterestRate/12
local_balance = balance
upper_limit = balance*math.pow((1+mon_int),12)/12
print "local balance out while = " +str(local_balance)

while (local_balance >0 or local_balance < -0.01):
    local_balance = balance
    #print "Initial " +str(local_balance)
    print mon_payment
    for i in range(12):
        local_balance = local_balance - mon_payment
        local_balance = local_balance*(1+mon_int)
    
    print "Local_Balance = "+str(local_balance)
    if local_balance > 0:
        lower_limit = mon_payment
        mon_payment = (lower_limit +upper_limit)/2
        print 'lowerlimit'
        print mon_payment
    if local_balance < -0.0001:
        upper_limit = mon_payment
        mon_payment = (lower_limit +upper_limit)/2
        print "upper"
    if local_balance ==0:
        break
    

print mon_payment

print 'Lowest Paym1ent: '+str(round(mon_payment,2)) 