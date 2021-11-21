import string
letters = list(string.ascii_lowercase)
uppercase = list(string.ascii_uppercase)

def find_index(string, list):
    index = 0
    for element in list:
        if string == element:
            return index
        else:
            index += 1

def encrypt(string, shift):
    index = find_index(string, letters)
    index += shift
    while index > 25:
        index -= 26
    return letters[index]

def encrypt_uppercase(string, shift):
    index = find_index(string, uppercase)
    index += shift
    while index > 25:
        index -= 26
    return uppercase[index]

def decrypt(string, shift):
    index = find_index(string, letters)
    index -= shift
    while index < 0:
        index += 26
    return letters[index]

def decrypt_uppercase(string, shift):
    index = find_index(string, uppercase)
    index -= shift
    while index < 0:
        index += 26
    return uppercase[index]

go_again = 'yes'

while go_again == "yes":
    cipher_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = list(input("Type your message:\n"))
    shift_number = int(input("Type the shift number:\n"))

    if cipher_mode == "encode":
        message_index = 0
        for letter in message:
            if letter in letters:
                message[message_index] = encrypt(letter, shift_number)
            elif letter in uppercase:
                message[message_index] = encrypt_uppercase(letter, shift_number)
            message_index += 1
        result = "".join(message)
        print(f"Here's the encoded result: {result}")
    elif cipher_mode == "decode":
        message_index = 0
        for letter in message:
            if letter in letters:
                message[message_index] = decrypt(letter, shift_number)
            elif letter in uppercase:
                message[message_index] = decrypt_uppercase(letter, shift_number)
            message_index += 1
        result = "".join(message)
        print(f"Here's the decoded result: {result}")

    go_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()