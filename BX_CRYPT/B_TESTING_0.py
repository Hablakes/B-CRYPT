import base64
import os
import time

import pyfiglet
import tkinter
import tkinter.filedialog


def encrypt_file():
    encrypted_file = []
    b64_encrypted_file = []

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

    current_time = int(time.time())

    for enum_chars, chars in enumerate(get_bytes_from_files(user_file)):
        msg_chars = chars
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = ((msg_chars * 2) * key_chars) % 1114100
        encrypted_file.append(chr(randomize_alg))

    encrypted_msg_bytes = ''.join(encrypted_file).encode('utf-8')
    encoded_b64_encrypted_msg = base64.b64encode(encrypted_msg_bytes)

    for enum_chars, chars in enumerate(encoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(chars)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = (msg_chars * key_spin) * key_chars
        b64_encrypted_file.append(randomize_alg)

    rotation_mix = rotate_rotor(b64_encrypted_file, int(len(key)))

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
    b64_decrypted_file = []

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

    current_time = int(time.time())
    inverse_key = (int(len(key)) - int(len(key)) * 2)

    with open(user_file, encoding='utf-8') as f:

        for encrypted_numbers in f:
            encrypted_numbers_list.append(chr(int(encrypted_numbers.rstrip('\n'))))

    rotated_encrypted_message = rotate_rotor(''.join(encrypted_numbers_list), int(inverse_key))

    for enum_chars, encrypted_letters in enumerate(rotated_encrypted_message):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = int((msg_chars / key_spin) / key_chars) % 1114100
        decrypted_file.append(chr(randomize_alg))

    try:
        decoded_b64_encrypted_msg = base64.b64decode(''.join(decrypted_file))

    except (TypeError, ValueError, UnicodeDecodeError) as e:
        print("KEY ERROR: ", e)
        print()
        return

    for enum_chars, encrypted_letters in enumerate(decoded_b64_encrypted_msg.decode('utf-8')):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = int((msg_chars / 2) / key_chars)
        b64_decrypted_file.append(randomize_alg)

    with open(os.path.expanduser(r'~/{0}').format(user_file_filename), 'wb') as f:
        f.write(bytearray(b64_decrypted_file))

    print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
    sep()


def get_bytes_from_files(filename):
    input_bytes_amount_int = 1024
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


def run():
    print()
    input_option = input("1) ENCRYPT      -   2) DECRYPT: ")
    option = int(input_option)
    if int(option) == 1:
        encrypt_file()
    elif int(option) == 2:
        decrypt_file()


run()
