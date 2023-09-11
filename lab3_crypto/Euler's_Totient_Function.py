def euler_totient(n):
    phi = n  # Initialize phi to n
    
    # Check for prime factors and apply Euler's Totient formula
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            phi -= phi // p
        p += 1
    
    # If n is a prime greater than 1
    if n > 1:
        phi -= phi // n
    
    return phi

if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))
    if n < 1:
        print("Please enter a positive integer.")
    else:
        result = euler_totient(n)
        print(f"Phi({n}) = {result}")
