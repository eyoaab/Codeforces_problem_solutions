n,t = list(map(int,input().split()))
nums = list(map(int,input().split()))

ans = 0
running_sum = 0
left = 0

for right in range(len(nums)):
    running_sum += nums[right]
    if running_sum >t:
        while  running_sum > t:
            running_sum -= nums[left]
            left+=1
            
    ans = max(ans,right-left+1)        

print(ans)    