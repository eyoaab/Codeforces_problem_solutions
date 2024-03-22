string = input()
answer = string.count('4') + string.count('7')
flag = True
for i in str(answer):
    if i not in '47':
        flag=False
        break
if flag:
    print("YES")
else:
    print("NO")        