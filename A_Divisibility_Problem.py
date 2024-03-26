import math
t= int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    if a<=b:
        print(b-a)
    else: 
        reminder = math.ceil(a/b) 
        print((reminder * b)-a) 
