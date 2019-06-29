import math
import os
import random

import pyfiglet

from tkinter import *
from tkinter.filedialog import askopenfilename


def check_if_number_is_prime(num):
    if num < 2:
        return False

    for prime in LOW_PRIMES:
        if num == prime:
            return True

        if num % prime == 0:
            return False

    return check_primes_rabin_miller_method(num)


def check_primes_rabin_miller_method(num):
    if num % 2 == 0 or num < 2:
        return False

    if num == 3:
        return True

    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1

    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False

                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def find_mod_inverse(a, m):
    if greatest_common_denominator(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m


def generate_large_prime_number(key_size):
    while True:
        num = random.randrange(2 ** (key_size - 1), 2 ** key_size)

        if check_if_number_is_prime(num):
            return num


def generate_rsa_key(key_size):
    sep()
    username = input('ENTER NAME FOR RSA KEY: ')
    sep()

    p = 0
    q = 0

    while p == q:
        p = generate_large_prime_number(key_size)
        q = generate_large_prime_number(key_size)
    n = p * q

    r = (p - 1) * (q - 1)

    while True:

        e = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if greatest_common_denominator(e, r) == 1:
            break

    d = find_mod_inverse(e, r)

    public_key = (n, e)
    public_key_list = [public_key]
    private_key = (n, d)
    private_key_list = [private_key]

    with open(os.path.expanduser(r'~/{0}').format(username) + '_PUBLIC_KEY.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join('%s %s' % x for x in public_key_list))

    with open(os.path.expanduser(r'~/{0}').format(username) + '_PRIVATE_KEY.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join('%s %s' % x for x in private_key_list))


def get_primes_sieve_method(sieve_size):
    sieve = [True] * sieve_size
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i

    primes = []

    for i in range(sieve_size):
        if sieve[i]:
            primes.append(i)

    return primes


LOW_PRIMES = get_primes_sieve_method(100)


def greatest_common_denominator(a, b):
    while a != 0:
        a, b = b % a, a
    return b


def encrypt_file_rsa():
    encrypted_file = []
    keys_file = []

    print(pyfiglet.figlet_format('INPUT FILE TO ENCRYPT:', font='cybermedium'))
    sep()

    root = Tk()
    root.withdraw()
    root.update()
    file_to_encrypt = askopenfilename()
    root.destroy()
    file_to_encrypt_filename = file_to_encrypt.rsplit('/', 1)[-1]

    print('FILE SELECTED: ' + file_to_encrypt_filename)
    sep()
    print('INPUT PRIVATE KEY FILE:')
    sep()

    root = Tk()
    root.withdraw()
    root.update()
    private_key_file = askopenfilename()
    root.destroy()
    private_key_filename = private_key_file.rsplit('/', 1)[-1]

    print('KEY SELECTED: ' + private_key_filename)
    sep()

    with open(private_key_file, 'r', encoding='utf-8') as f:
        for keys_found in f:
            keys_file.append(keys_found)

    private_key = int(keys_file[0].split()[1])
    n = int(keys_file[0].split()[0])

    for chars in get_bytes_from_files(file_to_encrypt):
        rsa_private_key_cipher = (chars ** private_key) % n
        encrypted_file.append(rsa_private_key_cipher)

    with open(os.path.expanduser(r'~/{0}').format(file_to_encrypt_filename) + '.bc', 'w', encoding='utf-8') as f:
        for encrypted_numbers in encrypted_file:
            f.write(str(int(encrypted_numbers)))
            f.write('\n')
        f.close()

    print(pyfiglet.figlet_format('FILE ENCRYPTED SUCCESSFULLY', font='cybermedium'))
    sep()


def decrypt_file_rsa():
    encrypted_numbers_list = []
    decrypted_file = []
    keys_file = []

    print(pyfiglet.figlet_format('INPUT FILE TO DECRYPT:', font='cybermedium'))
    sep()

    root = Tk()
    root.withdraw()
    root.update()
    file_to_decrypt = askopenfilename()
    root.destroy()
    file_to_decrypt_filename = file_to_decrypt.rsplit('.', 1)[0].rsplit('/', 1)[-1]

    print('FILE SELECTED: ' + file_to_decrypt_filename)
    sep()
    print('INPUT PUBLIC KEY FILE:')
    sep()

    root = Tk()
    root.withdraw()
    root.update()
    public_key_file = askopenfilename()
    root.destroy()
    public_key_filename = public_key_file.rsplit('/', 1)[-1]

    print('KEY SELECTED: ' + public_key_filename)
    sep()

    with open(public_key_file, 'r', encoding='utf-8') as f:
        for keys_found in f:
            keys_file.append(keys_found)

    public_key = int(keys_file[0].split()[1])
    n = int(keys_file[0].split()[0])

    with open(file_to_decrypt, encoding='utf-8') as f:

        for encrypted_numbers in f:
            encrypted_numbers_list.append(int(encrypted_numbers.rstrip('\n')))

    for encrypted_letters in encrypted_numbers_list:
        rsa_public_key_cipher = (encrypted_letters ** public_key) % n
        decrypted_file.append(rsa_public_key_cipher)

    with open(os.path.expanduser(r'~/{0}').format(file_to_decrypt_filename), 'wb') as f:
        f.write(bytearray(decrypted_file))

    print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
    sep()


def get_bytes_from_files(filename):
    print()
    print('ENTER BYTE AMOUNT (BLOCK SIZE) TO SCAN WITH: ')
    print()
    print('DEFAULT BLOCK SIZE IS 1024 (1KB).  IF UNSURE, ENTER: "1024"')
    print()
    print('-' * 100)

    input_bytes_amount = input()
    input_bytes_amount_int = int(input_bytes_amount)

    with open(filename, 'rb') as f:

        while True:
            bytes_amount = f.read(input_bytes_amount_int)

            if bytes_amount:

                for bts in bytes_amount:
                    yield bts
            else:
                break


def sep():
    for item in '\n', '-' * 100, '\n':
        print(item)
