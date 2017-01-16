# Copyright (c) 2016-present, Deckard, SoCrowd GmbH.
# All rights reserved.

# Represent a number as a primax.
# Example of a primax:
#
#   20992335 = 3^1*5^1*7^2*13^4
#   Primax(20992335) =
#   3 5 7 13
#   1 1 2 4

import functools as ft

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
