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

