s = 'ocwhokkn'

count = 0
new_str = ''
local_str = s[0]
for i in range(1,len(s)):
    if local_str[-1] <= s[i]:
        local_str = local_str + s[i]
    else:
        if len(local_str) > len(new_str):
            new_str = local_str
        local_str = s[i]
    if len(local_str) > len(new_str):
        new_str = local_str
    
print new_str
