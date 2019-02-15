import math


def interface():
    print()
    print("-" * 80)
    print("___     ____ ____ _   _ ___  ___ ____    ___ ____ ____ _ ")
    print("|__] __ |    |__/  \_/  |__]  |  |  | __  |  |  | |  | | ")
    print("|__]    |___ |  \   |   |     |  |__|     |  |__| |__| |___")
    print()
    print("-" * 80)
    print()
    print("1) ENCRYPT A MESSAGE          2) DECRYPT A MESSAGE          3) EXIT")
    print()
    print("-" * 80)
    print()
    bct_input = input("ENTER OPTION #")
    print()
    print("-" * 80)
    print()
    if int(bct_input) == 1:
        input_message_and_encrypt()
    elif int(bct_input) == 2:
        decrypt_message()
    elif int(bct_input) == 3:
        exit()


def input_message_and_encrypt():
    encrypted_msg = []

    in_msg = input("ENTER MESSAGE TO ENCRYPT:")
    print()
    in_key = input("ENTER KEY:")
    key = in_key
    print()
    print('-' * 80)
    print()

    for enum, chars in enumerate(in_msg):
        msg_chars = ord(chars)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum, ",", "CHARACTER ORDER #: ", msg_chars)
        encrypted_msg.append(chr(randomize_alg))

    print()
    print("MESSAGE INPUT:", in_msg)
    print()
    print("KEY INPUT:", key)
    print()
    print('-' * 80)
    print()
    print("ENCRYPTED MESSAGE:", ''.join(encrypted_msg))


def decrypt_message():
    decrypted_msg = []

    in_msg = input("ENTER MESSAGE TO DECRYPT:")
    print()
    in_key = input("ENTER KEY:")
    key = in_key
    print()
    print('-' * 80)
    print()

    for enum, encrypted_letters in enumerate(in_msg):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = int((msg_chars / 2) / key_chars)
        decrypted_msg.append(chr(randomize_alg))

    for enum, encrypted_chars in enumerate(in_msg):
        print("ENCRYPTED MESSAGE CHARACTER #'s:", enum, "- ", ord(encrypted_chars))
    print()
    print("KEY INPUT:", key)
    print()
    print('-' * 80)
    print()
    print("DECRYPTED MESSAGE:", ''.join(decrypted_msg))


while True:
    interface()
