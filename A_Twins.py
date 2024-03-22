from bisect import bisect_right
t = int(input())
nums = list(map(int,input().split()))
nums.sort(reverse = True)
halph = sum(nums)//2

prefix=[0]
for num in nums:
    prefix.append(num + prefix[-1])

answer = bisect_right(prefix,halph)
print(answer)

