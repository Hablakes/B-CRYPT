def interface():
    print()
    print('-' * 100)
    print()
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
        message_characters = int(ord(characters))
        key_characters = int(ord(key[enumeration_number % len(key)]))
        multiplied_msg_key_integer = int(((message_characters * 2) * key_characters)) % 1000000

        print()
        print("ENUMERATION #: ", enumeration_number)
        print()
        print("MSG CHARACTER: ", characters, " - ", "MESSAGE-CHARACTER ORDER #: ", message_characters)
        print("KEY CHARACTER: ", chr(key_characters), " - ", "KEY-CHARACTER ORDER #: ", key_characters)
        print()
        print("(MESSAGE-CHARACTER-ORDER * 2) * KEY-CHARACTER-ORDER #: ", chr(multiplied_msg_key_integer), " - ",
              multiplied_msg_key_integer)
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
        message_characters = int(ord(encrypted_letters))
        key_characters = int(ord(key[enumeration_number % len(key)]))
        divided_msg_key_integer = int((message_characters / 2) / key_characters) % 1000000

        print()
        print("ENUMERATION #: ", enumeration_number)
        print()
        print("MSG CHARACTER: ", encrypted_letters, " - ", "MESSAGE-CHARACTER ORDER #: ", message_characters)
        print("KEY CHARACTER: ", chr(key_characters), " - ", "KEY-CHARACTER ORDER #: ", key_characters)
        print()
        print("(MESSAGE-CHARACTER-ORDER / 2) / KEY-CHARACTER-ORDER #: ", chr(divided_msg_key_integer), " - ",
              divided_msg_key_integer)
        print()
        print('-' * 100)

        decrypted_msg.append(chr(divided_msg_key_integer))

    print()
    print()
    print()
    print("KEY INPUT: ", key)
    print()
    print("DECRYPTED MESSAGE: ", ''.join(decrypted_msg))


while True:
    interface()
