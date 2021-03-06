# Represent a number as a primax.
# Example of a primax:
#
#   20992335 = 3^1*5^1*7^2*13^4
#   Primax(20992335) =
#   3 5 7 13
#   1 1 2 4

import functools as ft
import encoder as enc

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

def getPrimax(n):
    ret= {}
    primfac = []
    d = 2

    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)

    uniqueVals = set(primfac)

    for i in uniqueVals:
        ret[i] = 0
    for i in primfac:
        ret[i] = ret[i] + 1

    return ret

print(getPrimax(20992335))

#test for a list of primes
for i in get_primes(5):
    enc.encodePrimax(getPrimax(i), str(i) + ".bmp","dist")

for i in range(1000,1100):
    pri = getPrimax(i)
    print(pri)
    #enc.encodePrimax(pri, str(i) + "-dist.bmp","dist")
    enc.encodePrimax(pri, str(i) + "-bright.bmp","bright2")
