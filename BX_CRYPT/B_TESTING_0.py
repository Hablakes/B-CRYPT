import math
import os
import random


test_re = '[0-9]+([0-9]+)*'


def testing_math():
    file_to_encrypt = r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/TEST.txt'

    for chars in get_bytes_from_files(file_to_encrypt):
        print(chars)

    print()
    test_number = input("INPUT BYTE # TO TEST: ")
    print()
    test_key_p = input("INPUT KEY # TO TEST: ")
    print()
    test_key_n = input("INPUT N # TO TEST: ")
    print()
    rsa_test = (int(test_number) ** int(test_key_p)) % int(test_key_n)

    print(rsa_test)
    print()


def testing_encrypt():
    encrypted_file = []
    keys_file = []

    private_key_file = r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/B_PUBLIC_KEY.txt'
    file_to_encrypt = r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/TEST.txt'

    with open(private_key_file, 'r', encoding='utf-8') as f:
        for keys_found in f:
            keys_file.append(keys_found)

    public_key = int(keys_file[0].split()[1])
    n = int(keys_file[0].split()[0])

    for chars in get_bytes_from_files(file_to_encrypt):
        rsa_public_key_cipher = (chars ** public_key) % n
        encrypted_file.append(rsa_public_key_cipher)

    with open(r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/TEST.txt' + '.bc', 'w', encoding='utf-8') as f:
        for encrypted_numbers in encrypted_file:
            f.write(str(int(encrypted_numbers)))
            f.write('\n')
        f.close()


def testing_decrypt():
    encrypted_numbers_list = []
    decrypted_file_list = []
    keys_file = []

    public_key_file = r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/B_PRIVATE_KEY.txt'
    file_to_decrypt = r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/TEST.txt.bc'

    with open(public_key_file, 'r', encoding='utf-8') as f:
        for keys_found in f:
            keys_file.append(keys_found)

    public_key = int(keys_file[0].split()[1])
    n = int(keys_file[0].split()[0])

    with open(file_to_decrypt, encoding='utf-8') as f:

        for encrypted_numbers in f:
            encrypted_numbers_list.append(int(encrypted_numbers.rstrip('\n')))

    for encrypted_letters in encrypted_numbers_list:
        rsa_private_key_cipher = (encrypted_letters ** public_key) % n
        decrypted_file_list.append(rsa_private_key_cipher)

    with open(r'/home/bx/PycharmProjects/B_TESTING/BX_CRYPT/TEST.txt.ubc', 'wb') as f:
        f.write(bytearray(decrypted_file_list))


def get_bytes_from_files(filename):
    input_bytes_amount_int = 64

    with open(filename, 'rb') as f:

        while True:
            bytes_amount = f.read(input_bytes_amount_int)

            if bytes_amount:

                for bts in bytes_amount:
                    yield bts
            else:
                break


def run():
    print()
    print("STARTING ENCRYPTION")
    print()
    testing_encrypt()
    print()
    print("ENCRYPTION COMPLETE / STARTING DECRYPTION")
    print()
    testing_decrypt()
    print()
    print("ENCRYPTION COMPLETE")
    print()


run()
