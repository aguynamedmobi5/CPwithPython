# Bitwise Operator

# and &
# or |
# not ~
# xor ^
# right shift >>  [Divides in power of 2]   [400 >> 4 = 400 // 2**4 = 25]
# left shift <<   [Multiply in power of 2]  [400 << 4 = 400 * (2**4) = 6400]

# Even Odd through Bitwise 'And' Operator

def evenodd(n):  # O(n)
    if n & 1 == 1:
        print("Odd")
    else:
        print("Even")


t = int(input())

while t:
    n = int(input())
    evenodd(n)
    t = t-1
