s= input()
if s==s.upper() or (s[0].islower() and s[1:]==s[1:].upper()):
    li=[]
    for i in s:
        li.append(i.swapcase())
    print(''.join(li))
else:
    print(s)            
           