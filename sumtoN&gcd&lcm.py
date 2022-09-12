######## Sum of N natural numbers #########################
"""
def sum(n):
    return (n)*(n+1) // 2


t = int(input())

while t:
    n = int(input())
    print(sum(n))
    t = t-1
"""
######## GCD and LCM #########################

# euclid algorithm
# O(log(min(a,b)))


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    prod = a*b
    hcf = gcd(a, b)
    return prod // hcf


t = int(input())

while t:
    n, m = map(int, input().split())
    print(f"GCD is: {gcd(n,m)}")
    print(f"LCM is: {lcm(n,m)}")
    t = t-1
