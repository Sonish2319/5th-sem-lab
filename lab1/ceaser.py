text = "SONISH UPADHYAYA"      
key = int(input("Enter the key: "))
    

#Encryption

def encrypt(text,key):
    cipher = ""
    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            cipher += chr((ord(char) + key -65) % 26 + 65)

        #elif(char == " "):
#            cipher +=  " "

        else:
            cipher += chr((ord(char) + key -97) % 26 + 65)

    return cipher
        
cipherText = encrypt(text, key)
print("Cipher Text:" + cipherText)

#Decryption

def decrypt(cipher,key):
    plain = ""

    for i in range(len(cipher)):
        char = cipher[i]

        if(char.isupper()):
            plain += chr((ord(char) - key - 65) % 26 + 65)

        #elif(char == " "):
         #   plain += " "

        else:
            plain += chr((ord(char) - key - 97) % 26 + 65)
    return plain

print("Decrypted Text: " + decrypt(cipherText,key))