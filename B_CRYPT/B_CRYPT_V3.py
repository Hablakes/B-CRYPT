import os


def interface():
    print()
    print("-" * 80)
    print("___     ____ ____ _   _ ___  ___ ____    ___ ____ ____ _")
    print("|__] __ |    |__/  \_/  |__]  |  |  | __  |  |  | |  | |")
    print("|__]    |___ |  \   |   |     |  |__|     |  |__| |__| |__")
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
        encrypt_file()
    elif int(bct_input) == 2:
        decrypt_file()
    elif int(bct_input) == 3:
        exit()


def get_bytes_from_files(filename):
    with open(filename, "rb") as f:
        while True:
            bytes_amount = f.read(1024)
            if bytes_amount:
                for bts in bytes_amount:
                    yield bts
            else:
                break


def encrypt_file():
    encrypted_file = []
    print("INPUT COMPLETE PATH OF FILE TO ENCRYPT:")
    print()
    file_to_encrypt = input()
    file_to_encrypt_filename = file_to_encrypt.rsplit('/', 1)[-1]
    print()
    print("-"*80)
    print()
    print("ENTER KEY:")
    print()
    in_key = input()
    key = in_key

    for enum, chars in enumerate(get_bytes_from_files(file_to_encrypt)):
        msg_chars = ord(chr(chars))
        key_chars = ord(key[enum % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        encrypted_file.append(chr(randomize_alg))

    with open(os.path.expanduser(r'~/{0}').format(file_to_encrypt_filename) + '.bc', 'w', encoding='UTF8') as f:
        f.write(''.join(encrypted_file))


def decrypt_file():
    decrypted_file = []
    print("INPUT COMPLETE PATH OF FILE TO DECRYPT:")
    print()
    file_to_decrypt = input()
    file_to_decrypt_original_filename = file_to_decrypt.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print()
    print("ENTER KEY:")
    print()
    in_key = input()
    key = in_key

    with open(file_to_decrypt) as f:
        for chars in f:
            for enum, encrypted_letters in enumerate(chars):
                msg_chars = ord(encrypted_letters)
                key_chars = ord(key[enum % len(key)])
                randomize_alg = int((msg_chars / 2) / key_chars)
                decrypted_file.append(randomize_alg)

    with open(os.path.expanduser(r'~/{0}').format(file_to_decrypt_original_filename), 'wb') as f:
        f.write(bytearray(decrypted_file))


while True:
    interface()
