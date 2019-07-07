def interface():
    print()
    print('-' * 100)
    print("____ ____ _   _ ___  ___ ____    ___ ____ ____ _ ")
    print("|    |__/  \_/  |__]  |  |  | __  |  |  | |  | | ")
    print("|___ |  \   |   |     |  |__|     |  |__| |__| |___")
    print()
    print('-' * 100)
    print()
    print("1) ENCRYPT A MESSAGE          2) DECRYPT A MESSAGE          3) EXIT")
    print()
    print('-' * 100)
    print()
    bct_input = input("ENTER OPTION #: ")
    print()
    print('-' * 100)
    print()
    if int(bct_input) == 1:
        input_message_and_encrypt()
    elif int(bct_input) == 2:
        decrypt_message()
    elif int(bct_input) == 3:
        exit()


def input_message_and_encrypt():
    encrypted_msg = []

    message = input("ENTER MESSAGE TO ENCRYPT: ")
    print()
    key = input("ENTER KEY: ")
    print()
    print('-' * 100)
    print()

    for enumeration_number, characters in enumerate(message):
        message_characters = ord(characters)
        key_characters = ord(key[enumeration_number % len(key)])
        multiplied_msg_key_integer = (message_characters * 2) * key_characters

        print()
        print("ENUMERATION #: ", enumeration_number)
        print("CHARACTER: ", characters, "- ", "MESSAGE-CHARACTER ORDER #: ", message_characters)
        print("KEY CHARACTERS: ", chr(key_characters), "- ", "KEY-CHARACTER ORDER #: ", key_characters)
        print()
        print("MULTIPLIED MESSAGE-CHARACTER-ORDER * KEY-CHARACTER-ORDER #: ", multiplied_msg_key_integer)
        print()
        print('-' * 100)

        encrypted_msg.append(chr(multiplied_msg_key_integer))

    print()
    print()
    print()
    print("MESSAGE INPUT: ", message)
    print()
    print("KEY INPUT: ", key)
    print()
    print("ENCRYPTED MESSAGE: ", ''.join(encrypted_msg))


def decrypt_message():
    decrypted_msg = []

    message = input("ENTER MESSAGE TO DECRYPT: ")
    print()
    key = input("ENTER KEY: ")
    print()
    print('-' * 100)
    print()

    for enumeration_number, encrypted_letters in enumerate(message):
        message_characters = ord(encrypted_letters)
        key_characters = ord(key[enumeration_number % len(key)])
        multiplied_msg_key_integer = int((message_characters / 2) / key_characters)

        decrypted_msg.append(chr(multiplied_msg_key_integer))

    for enumeration_number, encrypted_chars in enumerate(message):
        print("ENCRYPTED MESSAGE CHARACTER #'s: ", enumeration_number, "- ", encrypted_chars, "- ",
              ord(encrypted_chars))

    print()
    print("KEY INPUT: ", key)
    print()
    print('-' * 100)
    print()
    print("DECRYPTED MESSAGE: ", ''.join(decrypted_msg))


while True:
    interface()
