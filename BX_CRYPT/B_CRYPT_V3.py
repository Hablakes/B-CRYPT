import base64
import os
import textwrap

from tkinter import *
from tkinter.filedialog import askopenfilename


def interface():
    print()
    print("-" * 80)
    print("___     ____ ____ _   _ ___  ___ ____    ___ ____ ____ _  ")
    print("|__] __ |    |__/  \_/  |__]  |  |  | __  |  |  | |  | |  ")
    print("|__]    |___ |  \   |   |     |  |__|     |  |__| |__| |__")
    print()
    print("-" * 80)
    print()
    print("1) ENCRYPT A MESSAGE     2) DECRYPT A MESSAGE")
    print()
    print("3) ENCRYPT A FILE        4) DECRYPT A FILE           5) EXIT")
    print()
    print("-" * 80)
    print()
    bct_input = input("ENTER OPTION #")
    print()
    print("-" * 80)
    print()
    if int(bct_input) == 1:
        encrypt_message()
    elif int(bct_input) == 2:
        decrypt_message()
    elif int(bct_input) == 3:
        encrypt_file()
    elif int(bct_input) == 4:
        decrypt_file()
    elif int(bct_input) == 5:
        exit()


def encrypt_message():
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

    for enum_chars, chars in enumerate(in_msg):
        msg_chars = ord(chars)
        key_chars = ord(key[enum_chars % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum_chars, ",", "CHARACTER ORDER #: ", msg_chars)
        encrypted_msg.append(chr(randomize_alg))

    encrypted_msg_bytes = ''.join(encrypted_msg).encode("utf-8")
    print()
    print('-' * 80)
    print()
    encoded_b64_encrypted_msg = base64.b64encode(encrypted_msg_bytes)

    for enum_chars, chars in enumerate(encoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(chars)
        key_chars = ord(key[enum_chars % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum_chars, ",", "CHARACTER ORDER #: ", msg_chars)
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

    for enum_chars, encrypted_letters in enumerate(in_msg):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])
        randomize_alg = int((msg_chars / 2) / key_chars)
        decrypted_msg_s1.append(chr(randomize_alg))

    decoded_b64_encrypted_msg = base64.b64decode(''.join(decrypted_msg_s1))

    for enum_chars, encrypted_letters in enumerate(decoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])
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


def encrypt_file():
    encrypted_file = []
    print("INPUT COMPLETE PATH OF FILE TO ENCRYPT:")
    print()
    root = Tk()
    root.withdraw()
    root.update()
    file_to_encrypt = askopenfilename()
    root.destroy()
    # file_to_encrypt = input().replace('\\', '/')
    file_to_encrypt_filename = file_to_encrypt.rsplit('/', 1)[-1]
    print("-"*80)
    print()
    print("ENTER KEY:")
    in_key = input()
    key = in_key
    print()
    print("-" * 80)

    for enum_chars, chars in enumerate(get_bytes_from_files(file_to_encrypt)):
        msg_chars = ord(chr(chars))
        key_chars = ord(key[enum_chars % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        encrypted_file.append(chr(randomize_alg))

    with open(os.path.expanduser(r'~/{0}').format(file_to_encrypt_filename) + '.bc', 'w', encoding='UTF8') as f:
        f.write(''.join(encrypted_file))

    print()
    print("FILE ENCRYPTED SUCCESSFULLY")


def decrypt_file():
    decrypted_file = []
    print("INPUT COMPLETE PATH OF FILE TO DECRYPT:")
    print()
    root = Tk()
    root.withdraw()
    root.update()
    file_to_decrypt = askopenfilename()
    root.destroy()
    # file_to_decrypt = input().replace('\\', '/')
    file_to_decrypt_original_filename = file_to_decrypt.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print("-" * 80)
    print()
    print("ENTER KEY:")
    in_key = input()
    key = in_key
    print()
    print("-" * 80)

    with open(file_to_decrypt, encoding='UTF8') as f:
        for chars in f:
            for enum_chars, encrypted_letters in enumerate(chars):
                msg_chars = ord(encrypted_letters)
                key_chars = ord(key[enum_chars % len(key)])
                randomize_alg = int((msg_chars / 2) / key_chars)
                decrypted_file.append(randomize_alg)

    with open(os.path.expanduser(r'~/{0}').format(file_to_decrypt_original_filename), 'wb') as f:
        f.write(bytearray(decrypted_file))

    print()
    print("FILE DECRYPTED SUCCESSFULLY")


def get_bytes_from_files(filename):
    print()
    print("ENTER BYTE AMOUNT (BLOCK SIZE) TO SCAN WITH:")
    print()
    print("DEFAULT BLOCK SIZE IS 1024 / 1KB.  IF UNSURE, ENTER: '1024'")
    print()
    print("-" * 80)
    input_bytes_amount = input()
    input_bytes_amount_int = int(input_bytes_amount)
    with open(filename, "rb") as f:
        while True:
            bytes_amount = f.read(input_bytes_amount_int)
            if bytes_amount:
                for bts in bytes_amount:
                    yield bts
            else:
                break


while True:
    interface()
