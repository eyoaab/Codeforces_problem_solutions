n = int(input())
answer = 0

def cheack(num):
    count = set()
    d = 2
    while num > 1:
        if num%d == 0:
            count.appen(num%d)   

               
    return True        
for i in range(1,n+1):
    if cheack(i):
        answer +=1
print(answer)        
