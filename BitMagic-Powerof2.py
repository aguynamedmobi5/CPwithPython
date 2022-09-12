# Is Power Of 2

def isPowerOf2(n):
    if n <= 0:
        return False
    x = n
    y = not(n & (n-1))
    return x and y

######################################################

# Return number of 1's in binary representation of int
# 5 -> 101 --> 2
# 7 -> 111 --> 3


def cntbits(n):
    cnt = 0
    while n:
        cnt += 1
        n = n & (n-1)
    return cnt


t = int(input())

while t:
    n = int(input())
    # print(isPowerOf2(n))
    # print(cntbits(n))
    t = t-1
