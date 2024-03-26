n =int(input())
answer = 0
while n >0:
    if n>=100:
        answer += n //100
        n=n%100
    elif n>=20:
        answer += n //20
        n=n%20 
    elif n>=10:
        answer += n //10
        n=n%10  
    elif n>=5:
        answer += n //5
        n=n%5
    else:
        answer += n
        
        break    
print(answer)