t = int(input())
for _ in range(t):
    n=int(input())
    nums = list(map(int,input().split()))
    answer=0
    count_ = 0
    for i in range(len(nums)):
        if nums[i]>=i:
            count_ +=1
        else:
            count = 0    

        answer += count_
    print(answer)       
