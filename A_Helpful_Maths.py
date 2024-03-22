string = input().split('+')
nums = [int(i) for i in string]
nums.sort()
print('+'.join([str(i) for i in nums]))