# Paste your code into this box
lw=0
up=100
m= (lw+up)/2
print 'Please think of a number between 0 and 100!'
print 'Is your secret number' + str(m)+'?'
print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
ip = raw_input()
while ip != 'c':
    if ip == 'h':
        up =m
        m= round((lw+up)/2)
    elif ip == 'l':
        lw = m
        m = round((lw+up)/2)
    else:
        print 'Sorry, I did not understand your input.'
    print 'Is your secret number' + str(int(m))+'?'
    print "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",
    ip = raw_input()
if ip == 'c':
    print "Game over. Your secret number was: ", int(m)

    
        
