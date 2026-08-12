def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# ---------------- MAIN PROGRAM ----------------

for i in range (10):
    g=1
    

    
    print("enter (x) for exit ")
    plain_text = input("Enter Plain Text: ")
    
    if plain_text=="x":
        a=1
    else:    
        shift = int(input("Enter Shift Key: "))

        encrypted = caesar_encrypt(plain_text, shift)
        print("\nEncrypted Text:", encrypted)

        decrypted = caesar_decrypt(encrypted, shift)
        print("Decrypted Text:", decrypted)

    print("\n\n\n\n\n")

