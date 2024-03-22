n = int(input())
nums = list(map(int,input().split()))

answer = sum(nums)/n
print("%.12f"% answer)