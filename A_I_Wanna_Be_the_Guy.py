n = int(input())
nums1 = list(map(int,input().split()))
nums2 = list(map(int,input().split()))
answer = set(nums1[1:]+ nums2[1:])
flag = True
for i in range(1,n+1):
    if i not in answer:
        flag = False
        break
if flag:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")    

