import base64
import os
import textwrap

import pyfiglet
import tkinter
import tkinter.filedialog


def main():
    while True:
        interface()


def interface():
    print('-' * 100)
    print(pyfiglet.figlet_format('B-CRYPTO-TOOL', font='cybermedium'))
    print('-' * 100)
    print()
    print()
    print('SYMMETRICAL KEY ENCRYPTION OPTIONS:')
    print()
    print('1) ENCRYPT A MESSAGE         2) DECRYPT A MESSAGE')
    print()
    print('3) ENCRYPT A FILE            4) DECRYPT A FILE')
    sep()
    print('ASYMMETRICAL KEY ENCRYPTION OPTIONS:')
    print()
    print('5) ENCRYPT A FILE            6) DECRYPT A FILE')
    print()
    print('7) GENERATE NEW RSA KEYS     8) EXIT')
    sep()
    bct_input = input('ENTER OPTION #: ')
    sep()

    if int(bct_input) == 1:
        encrypt_message()
    elif int(bct_input) == 2:
        decrypt_message()
    elif int(bct_input) == 3:
        encrypt_file()
    elif int(bct_input) == 4:
        decrypt_file()
    elif int(bct_input) == 5:
        pass
    elif int(bct_input) == 6:
        pass
    elif int(bct_input) == 7:
        pass
    elif int(bct_input) == 8:
        exit()


def encrypt_message():
    encrypted_msg = []
    b64_encrypted_msg = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO ENCRYPT:', font='cybermedium'))
    sep()
    in_msg = input()
    print('-' * 100)
    print()
    in_key = input('ENTER KEY: ')
    key = in_key
    sep()

    key_spin = int(len(key)) % 6

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    for enum_chars, chars in enumerate(in_msg):
        msg_chars = ord(chars)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = (msg_chars * 2) * key_chars
        encrypted_msg.append(chr(randomize_alg))

    encrypted_msg_bytes = ''.join(encrypted_msg).encode('utf-8')
    encoded_b64_encrypted_msg = base64.b64encode(encrypted_msg_bytes)

    for enum_chars, chars in enumerate(encoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(chars)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = (msg_chars * key_spin) * key_chars
        b64_encrypted_msg.append(chr(randomize_alg))

    print()
    print('MESSAGE INPUT: ', in_msg)
    print()
    print('KEY INPUT: ', key)
    sep()
    print('ROTATED / FINAL ENCRYPTED MESSAGE: ')
    print()
    print(rotate_rotor(''.join(b64_encrypted_msg), int(len(key))))
    sep()


def decrypt_message():
    decrypted_msg = []
    b64_decrypted_msg = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO DECRYPT:', font='cybermedium'))
    sep()
    in_msg = input()
    print('-' * 100)
    print()
    in_key = input('ENTER KEY: ')
    key = in_key
    sep()

    key_spin = int(len(key)) % 6

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    inverse_key = (int(len(key)) - int(len(key)) * 2)

    rotated_encrypted_message = rotate_rotor(''.join(in_msg), int(inverse_key))

    for enum_chars, encrypted_letters in enumerate(rotated_encrypted_message):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = int((msg_chars / key_spin) / key_chars)
        decrypted_msg.append(chr(randomize_alg))

    try:
        decoded_b64_encrypted_msg = base64.b64decode(''.join(decrypted_msg))

    except (TypeError, ValueError, UnicodeDecodeError) as e:
        print("KEY ERROR: ", e)
        print()
        return

    for enum_chars, encrypted_letters in enumerate(decoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = int((msg_chars / 2) / key_chars)
        b64_decrypted_msg.append(chr(randomize_alg))

    print()
    print('KEY INPUT: ', key)
    sep()
    print('DECRYPTED MESSAGE: ')
    print()
    print(textwrap.fill(''.join(b64_decrypted_msg), 100))
    sep()


def encrypt_file():
    encrypted_file = []

    print(pyfiglet.figlet_format('INPUT FILE TO ENCRYPT:', font='cybermedium'))
    sep()
    user_file = tk_gui_file_selection_window()
    user_file_filename = user_file.rsplit('/', 1)[-1]
    print("FILE SELECTED: ",  user_file_filename)
    sep()
    in_key = input('ENTER KEY: ')
    key = in_key
    sep()

    key_spin = int(len(key)) % 6

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    for enum_chars, chars in enumerate(get_bytes_from_files(user_file)):
        msg_chars = ord(chr(chars))
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = ((msg_chars * key_spin) * key_chars) % 1114100
        encrypted_file.append(randomize_alg)

    rotation_mix = rotate_rotor(encrypted_file, int(len(key)))

    with open(os.path.expanduser(r'~/{0}').format(user_file_filename) + '.bc', 'w', encoding='utf-8') as f:
        for encrypted_numbers in rotation_mix:
            f.write(str(int(encrypted_numbers)))
            f.write('\n')
        f.close()

    print(pyfiglet.figlet_format('FILE ENCRYPTED SUCCESSFULLY', font='cybermedium'))
    sep()


def decrypt_file():
    encrypted_numbers_list = []
    decrypted_file = []

    print(pyfiglet.figlet_format('INPUT FILE TO DECRYPT:', font='cybermedium'))
    sep()
    user_file = tk_gui_file_selection_window()
    user_file_filename = user_file.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print("FILE SELECTED: ",  user_file_filename)
    sep()
    in_key = input('ENTER KEY: ')
    key = in_key
    sep()

    key_spin = int(len(key)) % 6

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    inverse_key = (int(len(key)) - int(len(key)) * 2)

    with open(user_file, encoding='utf-8') as f:

        for encrypted_numbers in f:
            encrypted_numbers_list.append(chr(int(encrypted_numbers.rstrip('\n'))))

    rotated_encrypted_message = rotate_rotor(''.join(encrypted_numbers_list), int(inverse_key))

    for enum_chars, encrypted_letters in enumerate(rotated_encrypted_message):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = int((msg_chars / key_spin) / key_chars) % 1114100
        decrypted_file.append(randomize_alg)

    with open(os.path.expanduser(r'~/{0}').format(user_file_filename), 'wb') as f:
        f.write(bytearray(decrypted_file))

    print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
    sep()


def get_bytes_from_files(filename):
    print()
    print('ENTER BYTE AMOUNT (BLOCK SIZE) TO SCAN WITH: ')
    print()
    print('DEFAULT BLOCK SIZE IS 1024 (1KB).  IF UNSURE, ENTER: "1024"')
    sep()
    input_bytes_amount = input()
    input_bytes_amount_int = int(input_bytes_amount)
    sep()
    with open(filename, 'rb') as f:

        while True:
            bytes_amount = f.read(input_bytes_amount_int)

            if bytes_amount:

                for bts in bytes_amount:
                    yield bts
            else:
                break


def rotate_rotor(alphabet, rotations):
    return alphabet[rotations:] + alphabet[:rotations]


def sep():
    for item in '\n', '-' * 100, '\n':
        print(item)


def tk_gui_file_selection_window():
    root = tkinter.Tk()
    root.withdraw()
    root.update()
    selected_file = tkinter.filedialog.askopenfilename()
    root.destroy()
    return selected_file


if __name__ == '__main__':
    main()
