import random

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1  # y = y/2
        x = (x * x) % p
    return res

def miillerTest(d, n):
    a = 2 + random.randint(1, n - 4)
    x = power(a, d, n)
    if x == 1 or x == n - 1:
        return True
    while d != n - 1:
        x = (x * x) % n
        d *= 2
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False

def isPrime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Find the largest power of 2 that divides n-1
    d = n - 1
    while d % 2 == 0:
        d //= 2

    # Witness loop
    for _ in range(k):
        if not miillerTest(d, n):
            return False
    return True

if __name__ == "__main__":
    n = int(input("Enter a number to check for primality: "))
    k = int(input("Enter the number of iterations (recommended 5): "))
    
    if isPrime(n, k):
        print(f"{n} is likely to be prime.")
    else:
        print(f"{n} is not prime.")
