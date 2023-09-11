import random
import sympy

# Function to generate random prime numbers
def generate_prime(bits):
    while True:
        num = random.getrandbits(bits)
        if sympy.isprime(num):
            return num

# Function to compute the modular multiplicative inverse (a^(-1) mod m)
def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError("The modular inverse does not exist.")
    return x % m

# Extended Euclidean Algorithm to find the modular inverse
def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

# Function to generate RSA keys
def generate_rsa_keys(bits):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)

    while True:
        e = random.randint(2, phi - 1)
        if sympy.isprime(e) and sympy.gcd(e, phi) == 1:
            break

    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in message]
    return cipher_text

# Function to decrypt a message
def decrypt(cipher_text, private_key):
    d, n = private_key
    plain_text = [chr(pow(char, d, n)) for char in cipher_text]
    return ''.join(plain_text)

if __name__ == "__main__":
    bits = 1024  # Adjust the key size as needed
    public_key, private_key = generate_rsa_keys(bits)

    message = "Hello, RSA!"
    print("Original Message:", message)

    encrypted_message = encrypt(message, public_key)
    print("Encrypted Message:", encrypted_message)

    decrypted_message = decrypt(encrypted_message, private_key)
    print("Decrypted Message:", decrypted_message)
