n , height = list(map(int,input().split()))
nums = list(map(int,input().split()))
answer = 0

for num in  nums:
    if num > height:
        answer +=2
    else:
        answer += 1

print(answer)