age1,age2 = list(map(int,input().split()))
i=0
while True:
    if age1 > age2:
        print(i)
        break    
    age1 *= 3
    age2 *= 2
    i+=1