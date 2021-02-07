import nltk

# Encryption algo should:
# Check whether a letter
# If not letter, add the same to the cipher text without changing it
# If a letter, check whether upper or lower
# maintain the letter casing
# if traversal is greater than that of the alphabet, wrap to the beginning
# add new letter to the cipher


# def generate_key():
#     key = int(
#         input('Give Caesar a key.. a number between one and twenty-five please. >'))

#     while key < 1 or key > 25:
#         print("Invalid key. Enter a number between 1 and 25")
#         key = int(input())

#     print(f"Caesar has graciously generated {key} as your key")


def encrypt(text, key):
    encrypted_text = ''

    for char in text:
        # check if it's uppercase
        if char.isupper():
            char_index = ord(char) - ord('A')
            # shift current character by key position
            char_shifted = (char_index + key) % 26 + ord('A')
            new_char = chr(char_shifted)
            encrypted_text += new_char
        # check if it's lowercase
        elif char.islower():
            # subtract the unicode of 'a' to get index in 0-25 range
            char_index = ord(char) - ord('a')
            char_shifted = (char_index + key) % 26 + ord('a')
            new_char = chr(char_shifted)
            encrypted_text += new_char
        # check if it's a number
        elif char.isdigit():
            new_char = (int(char) + key) % 10
            encrypted_text += str(new_char)
        # if not a number or letter, leave it alone
        else:
            encrypted_text += char
    return encrypted_text


def decrypt(encoded, key):
    decrypted = ''

    for char in encoded:
        if char.isupper():
            char_index = ord(char) - ord('A')
            # shift current character to left by key positions to get original position
            char_og_pos = (char_index - key) % 26 + ord('A')
            char_og = chr(char_og_pos)
            decrypted += char_og
        elif char.islower():
            char_index = ord(char) - ord('a')
            char_og_pos = (char_index - key) % 26 + ord('a')
            char_og = chr(char_og_pos)
            decrypted += char_og
        elif char.isdigit():
            char_og = (int(char) - key) % 10
            decrypted += str(char_og)
        else:
            decrypted += char
    return decrypted


def crack():
    pass


if __name__ == "__main__":
    text = 'Its a trap! Watch your 6!'
    cipher = encrypt(text, 3)
    print(f"Plain text message: {text}")
    print(f"Encrypted message: {cipher}")

    encoded = 'Lwv d wuds! Zdwfk brxu 9!'
    decrypted_msg = decrypt(encoded, 3)
    print(f"Cipher text: {encoded}")
    print(f"Decrypted message: {decrypted_msg}")

    print(encrypt('zzz', 1))
    print(encrypt('abc', 27))
