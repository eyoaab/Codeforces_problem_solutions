n = int(input())
previous = '00'
answer = 1

for _ in range(n):
    num = input()
    if previous =='00':
        previous = num[1]
    else:
        if previous == num[0] :
            answer +=1
        previous = num[1]

print(answer)