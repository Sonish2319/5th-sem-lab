def generate_playfair_square(key):
    # Function to generate a Playfair square from the given key
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key + alphabet

    # Remove duplicate letters from the key
    key = "".join(dict.fromkeys(key))

    playfair_square = [['' for _ in range(5)] for _ in range(5)]
    row, col = 0, 0

    for letter in key:
        if col == 5:
            col = 0
            row += 1
        playfair_square[row][col] = letter
        col += 1

    return playfair_square

def find_letter_coordinates(square, letter):
    # Find the coordinates (row, col) of a letter in the Playfair square
    for i in range(5):
        for j in range(5):
            if square[i][j] == letter:
                return i, j

def encrypt_pair(square, pair):
    # Encrypt a pair of letters using the Playfair cipher rules
    a, b = pair[0], pair[1]
    row_a, col_a = find_letter_coordinates(square, a)
    row_b, col_b = find_letter_coordinates(square, b)

    if row_a == row_b:
        return square[row_a][(col_a + 1) % 5] + square[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        return square[(row_a + 1) % 5][col_a] + square[(row_b + 1) % 5][col_b]
    else:
        return square[row_a][col_b] + square[row_b][col_a]

def encrypt(message, square):
    # Encrypt the message using the Playfair cipher
    message = message.replace(" ", "").upper()

    # Handle repeated letters by replacing the second occurrence with 'X'
    i = 0
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message = message[:i + 1] + 'X' + message[i + 1:]
        i += 2

    # If the message length is odd, append 'X' at the end
    if len(message) % 2 != 0:
        message += 'X'

    encrypted_message = ""
    for i in range(0, len(message), 2):
        pair = message[i:i + 2]
        encrypted_message += encrypt_pair(square, pair)

    return encrypted_message

def decrypt_pair(square, pair):
    # Decrypt a pair of letters using the Playfair cipher rules
    a, b = pair[0], pair[1]
    row_a, col_a = find_letter_coordinates(square, a)
    row_b, col_b = find_letter_coordinates(square, b)

    if row_a == row_b:
        return square[row_a][(col_a - 1) % 5] + square[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return square[(row_a - 1) % 5][col_a] + square[(row_b - 1) % 5][col_b]
    else:
        return square[row_a][col_b] + square[row_b][col_a]

def decrypt(encrypted_message, square):
    # Decrypt the message using the Playfair cipher
    encrypted_message = encrypted_message.replace(" ", "").upper()

    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        pair = encrypted_message[i:i + 2]
        decrypted_message += decrypt_pair(square, pair)

    return decrypted_message

if __name__ == "__main__":
    # Get the user's full name
    full_name = input("Enter your full name: ")

    # Define the Playfair cipher key (avoid repeated letters)
    key = "ENCRYPTION"

    # Generate the Playfair square from the key
    playfair_square = generate_playfair_square(key)

    # Perform encryption
    encrypted_name = encrypt(full_name, playfair_square)
    print(f"Encrypted name: {encrypted_name}")

    # Perform decryption using the same encrypted text
    decrypted_name = decrypt(encrypted_name, playfair_square)
    print(f"Decrypted name: {decrypted_name}")