t = int(input())
answer=0
for _ in range(t):
    query = input()
    if query == 'X++' or query == '++X':
        answer += 1
    else:
        answer -= 1 
print(answer)           