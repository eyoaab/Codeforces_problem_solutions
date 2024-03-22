first = input()
second = input()
second = list(second)
left,right=0,len(second)-1

while left < right:
    second[left],second[right] = second[right],second[left]
    left += 1
    right -= 1
if len(second) != len(first) or ''.join(second) != first:
    print("NO")
else:
    print("YES")        
