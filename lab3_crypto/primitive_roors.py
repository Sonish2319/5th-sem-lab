def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_primitive_roots(p):
    if not is_prime(p):
        return None  # p must be a prime number

    phi_p = p - 1
    primitive_roots = []

    for a in range(2, p):
        if gcd(a, p) == 1:
            is_primitive_root = True
            for i in range(1, phi_p):
                if pow(a, i, p) == 1:
                    is_primitive_root = False
                    break
            if is_primitive_root:
                primitive_roots.append(a)

    return primitive_roots

if __name__ == "__main__":
    p = int(input("Enter a prime number (p): "))
    if is_prime(p):
        roots = find_primitive_roots(p)
        if roots:
            print(f"The primitive roots modulo {p} are:", roots)
        else:
            print(f"There are no primitive roots modulo {p}.")
    else:
        print("Please enter a prime number.")
