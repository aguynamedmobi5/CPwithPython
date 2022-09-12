from math import *


def primality1(n):  # O(n)
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter += 1

    if counter == 2:
        return True
    else:
        return False


def primality2(n):  # More efficient than primality1()
    if n == 0 or n == 1:  # O(1)
        return False
    if n == 2 or n == 3:  # O(1)
        return True
    if n % 2 == 0 or n % 3 == 0:  # O(1)
        return False
    for i in range(5, int(sqrt(n))+1):  # O(root n)
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True


t = int(input())

while t:
    n = int(input())
    print(primality1(n))
    print(primality2(n))

    t = t-1
