n = int(input())
answer = 0
current = 0

for _ in  range(n):
    out ,enter = list(map(int,input().split()))
    current -= out
    current += enter
    answer = max(answer,current)
print(answer)    
