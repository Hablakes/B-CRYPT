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
            bytes_amount = f.read(8)
            if bytes_amount:
                for bts in bytes_amount:
                    yield bts
            else:
                break


def encrypt_file():
    encrypted_msg = []
    b64_encrypted_msg = []
    print("-" * 80)
    print("INPUT COMPLETE PATH OF FILE TO ENCRYPT:")
    print()
    file_to_encrypt = input()
    print()
    print("-"*80)
    print()
    print("ENTER KEY:")
    print()
    in_key = input()
    key = in_key
    print()
    print('-' * 80)
    print()

    for enum, chars in enumerate(get_bytes_from_files(file_to_encrypt)):
        msg_chars = ord(chr(chars))
        key_chars = ord(key[enum % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        encrypted_msg.append(chr(randomize_alg))

    print(''.join(encrypted_msg))


def decrypt_file():
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
    print('-'*80)
    print()

    for enum, encrypted_letters in enumerate(in_msg):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = int((msg_chars / 2) / key_chars)
        decrypted_msg_s1.append(chr(randomize_alg))

    print("RESULTS:", ''.join(decrypted_msg_s1))


while True:
    interface()
