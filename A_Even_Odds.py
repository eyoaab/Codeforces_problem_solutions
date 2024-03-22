import math
n,k = list(map(int,input().split()))
pivot = math.ceil(n/2)

if k > pivot:
    k-=pivot
    print(2*k)
else:
    print((k*2)-1)    
