n,t = list(map(int,input().split()))
string = input()
string = list(string)

for _ in range(t):
    i = 1
    while i < len(string):
        if string[i]=='G' and string[i-1]=='B':
           string[i-1] = 'G'
           string[i] = 'B' 
           i += 2
        else:
            i+=1  
print(''.join(string))             