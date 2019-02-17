import base64
import textwrap


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
    b64_encrypted_msg = []

    print("ENTER MESSAGE TO ENCRYPT:")
    print()
    in_msg = input()
    print()
    print("ENTER KEY:")
    print()
    in_key = input()
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

    encrypted_msg_bytes = ''.join(encrypted_msg).encode("utf-8")
    print()
    print('-' * 80)
    print()
    encoded_b64_encrypted_msg = base64.b64encode(encrypted_msg_bytes)

    for enum, chars in enumerate(encoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(chars)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum, ",", "CHARACTER ORDER #: ", msg_chars)
        b64_encrypted_msg.append(chr(randomize_alg))

    print()
    print("MESSAGE INPUT:", in_msg)
    print()
    print("KEY INPUT:", key)
    print()
    print('-' * 80)
    print()
    print("ENCRYPTED MESSAGE:")
    print()
    print(textwrap.fill(''.join(encrypted_msg), 80))
    print()
    print("BASE 64 ENCODED ENCRYPTED MESSAGE:")
    print()
    print(textwrap.fill(encoded_b64_encrypted_msg.decode('utf-8'), 80))
    print()
    print("ENCRYPTED B64 MESSAGE:")
    print()
    print(''.join(b64_encrypted_msg))


def decrypt_message():
    decrypted_msg_s1 = []
    b64_decrypted_msg = []

    print("ENTER MESSAGE TO DECRYPT:")
    print()
    in_msg = input()
    print()
    print("ENTER KEY:")
    print()
    in_key = input()
    key = in_key
    print()
    print('-' * 80)
    print()

    for enum, encrypted_letters in enumerate(in_msg):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = int((msg_chars / 2) / key_chars)
        decrypted_msg_s1.append(chr(randomize_alg))

    decoded_b64_encrypted_msg = base64.b64decode(''.join(decrypted_msg_s1))

    for enum, encrypted_letters in enumerate(decoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = int((msg_chars / 2) / key_chars)
        b64_decrypted_msg.append(chr(randomize_alg))

    print()
    print("KEY INPUT:", key)
    print()
    print('-' * 80)
    print()
    print("DECRYPTED MESSAGE:")
    print()
    print(textwrap.fill(''.join(b64_decrypted_msg), 80))


while True:
    interface()
