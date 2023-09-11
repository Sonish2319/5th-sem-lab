import random

# Function to calculate modular exponentiation (a^b mod m)
def mod_exp(a, b, m):
    result = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        b = b // 2
        a = (a * a) % m
    return result

# Function to perform Diffie-Hellman key exchange
def diffie_hellman():
    # Publicly agreed upon prime modulus and base
    p = 23  # Prime modulus
    g = 5   # Base

    # Alice's private key (a)
    a = random.randint(2, p - 2)

    # Bob's private key (b)
    b = random.randint(2, p - 2)

    # Calculate Alice's public key (A = g^a mod p)
    A = mod_exp(g, a, p)

    # Calculate Bob's public key (B = g^b mod p)
    B = mod_exp(g, b, p)

    # Shared secret key for Alice (s = B^a mod p)
    secret_key_alice = mod_exp(B, a, p)

    # Shared secret key for Bob (s = A^b mod p)
    secret_key_bob = mod_exp(A, b, p)

    return secret_key_alice, secret_key_bob

if __name__ == "__main__":
    alice_key, bob_key = diffie_hellman()
    
    print("Alice's Secret Key:", alice_key)
    print("Bob's Secret Key:", bob_key)
