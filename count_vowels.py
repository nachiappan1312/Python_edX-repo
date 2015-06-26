s = 'azcbobobegghakl'

count = 0
while s:
    f = s.find('bob')
    if f != -1:
        s = s[f+1:]
        count += 1
    else:
        s =''
print count
    