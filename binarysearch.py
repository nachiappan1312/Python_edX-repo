def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''

    ret_var = False
    # Your code here
    strlen = len(aStr)
    print "Character " +char
    print "string " +aStr
    print strlen
    if strlen < 1:
        return False
    if strlen ==1 and aStr == char:
        return True
    elif strlen == 1 and not aStr == char:
        return False
    mid_char = aStr[strlen/2]
    print "midchar: " +mid_char
    if mid_char == char:
        return True
    elif char < mid_char:
        return isIn(char,aStr[:strlen/2])
    elif char > mid_char:
        return isIn(char,aStr[strlen/2:])
    else:
        ret_var = False
    return ret_var

print isIn('d', 'admqvyz')