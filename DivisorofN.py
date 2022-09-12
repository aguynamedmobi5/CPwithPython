# Divisors of N

from math import *


def divisor(n):
    div = set()
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            div.add(i)
            div.add(n//i)
    return list(div)


t = int(input())

while t:
    n = int(input())
    div = divisor(n)
    print(*div)
    t = t-1
