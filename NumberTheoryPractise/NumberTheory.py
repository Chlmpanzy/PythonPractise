import math
#Euclidean Algorithim GCD

def gcd(a,b):
    rem = b%a
    div = int(b/a)
    if rem == 0:
        return a
    return(gcd(rem, a))

#print(gcd(7,876543))

#list of divisors

def divisors1(n): # O(n)
    div = []
    for i in range(1, n+1):
        if n%i == 0:
            div.append(i)
    return div

def divisors2(n):
    div = []
    for i in range(1, int(math.sqrt(n)+1)):
        if n%i == 0:
            div.append(i)
            div.append(n//i)
    return sorted(div)

print(*divisors2(int(input(""))))


#Check for Prime

def checkPrime(n): #O(1) or [5, root(n)]
    if n == (0 or 1):
        return False
    if n ==(2 or 3):
        return True
    if n%(2 or 3) == 0:
        return False
    for i in range(5,int(math.sqrt(n))+1):
        if n%(i or (i+2)) == 0:
            return False
    return True

print(checkPrime(19))

#Seive Theorem

def primeList(n): #n*log(log(n))
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for p in range(2,int(math.sqrt(n))+1):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i] = False

    for i in range(0,len(primes)):
        if primes[i] == True:
            print(i, end=' ')

print(primeList(50))
