import base64
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

    current_time = int(time.time())

    key_spin = int(len(key)) % 6

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    for enum_chars, chars in enumerate(get_bytes_from_files(user_file)):
        msg_chars = ord(chr(chars))
        key_chars = ord(key[enum_chars % len(key)])

        randomize_alg = ((msg_chars * key_spin) * key_chars) % 1114100
        encrypted_file.append(chr(randomize_alg))

    for items in encrypted_file:
        print(items)


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


encrypt_file()
