n= int(input())
primes= [True]*n

primes[0]=primes[1]=False

i = 2
while i <= n:
    j = i*i 
    if primes[i]: 
        while j <= n:
            primes[j] = False
            j+=i
    else:
        i+=1
print(primes.count(True))        