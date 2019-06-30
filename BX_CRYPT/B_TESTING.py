import base64
import os
import textwrap
import time

import pyfiglet
import tkinter
import tkinter.filedialog


def main():
    while True:
        interface()


def interface():
    print('-' * 100)
    print(pyfiglet.figlet_format('BX-CRYPT', font='cybermedium'))
    print("*** TESTING BRANCH ***")
    print('-' * 100)
    print()
    print()
    print('SYMMETRICAL KEY ENCRYPTION OPTIONS: ')
    print()
    print('1) ENCRYPT A MESSAGE         2) DECRYPT A MESSAGE')
    print()
    print('3) ENCRYPT A FILE            4) DECRYPT A FILE')
    print()
    print('8) EXIT')
    separator()
    user_input = input('ENTER OPTION #: ')
    separator()

    if int(user_input) == 1:
        encrypt_message()
    elif int(user_input) == 2:
        decrypt_message()
    elif int(user_input) == 8:
        exit()


def encrypt_message():
    encrypted_message_list = []
    base64_encrypted_message_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO ENCRYPT: ', font='cybermedium'))
    separator()
    input_message = input('ENTER MESSAGE: ')
    separator()
    key = input('ENTER KEY: ')
    separator()
    key_spin = int(len(key)) % 6
    current_time = int(time.time())

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    time_spin = int(current_time) // (int(key_spin) * 2048)

    for character_enumeration_number, characters in enumerate(input_message):
        message_characters = ord(characters)
        key_characters = ord(key[character_enumeration_number % len(key)])
        random_characters = key_spin % message_characters
        randomize_algorithm = (message_characters * 2) * key_characters

        encrypted_message_list.append(chr(randomize_algorithm))
        print(characters, key_characters, key_spin, message_characters, randomize_algorithm, random_characters)

    encrypted_message_list_bytes = ''.join(encrypted_message_list).encode('utf-8')
    encoded_base64_encrypted_message = base64.b64encode(encrypted_message_list_bytes)

    for character_enumeration_number, characters in enumerate(encoded_base64_encrypted_message.decode('utf-8')):
        message_characters = ord(characters)
        key_characters = ord(key[character_enumeration_number % len(key)])
        randomize_algorithm = (message_characters * key_spin) * key_characters

        base64_encrypted_message_list.append(chr(randomize_algorithm))

    base64_encrypted_message_list.insert(int(key_spin), chr(int(time_spin)))
    rotated_encrypted_msg = rotate_rotor(''.join(base64_encrypted_message_list), int(len(key)))

    print()
    print('MESSAGE INPUT: ', input_message)
    print()
    print('KEY INPUT: ', key)
    separator()
    print('ROTATED / FINAL ENCRYPTED MESSAGE: ')
    print()
    print(rotated_encrypted_msg)
    separator()


def decrypt_message():
    rotated_encrypted_message_list = []
    base64_decrypted_message_list = []
    decrypted_message_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO DECRYPT: ', font='cybermedium'))
    separator()
    input_message = input('ENTER MESSAGE: ')
    separator()
    key = input('ENTER KEY: ')
    separator()
    key_spin = int(len(key)) % 6
    inverse_key = (int(len(key)) - int(len(key)) * 2)

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    rotated_encrypted_message = rotate_rotor(''.join(input_message), int(inverse_key))

    for characters in rotated_encrypted_message:
        rotated_encrypted_message_list.append(characters)

    time_spin_character = rotated_encrypted_message_list.pop(int(key_spin))

    for character_enumeration_number, encrypted_letters in enumerate(rotated_encrypted_message_list):
        message_characters = ord(encrypted_letters)
        key_characters = ord(key[character_enumeration_number % len(key)])
        randomize_algorithm = int((message_characters / key_spin) / key_characters)

        decrypted_message_list.append(chr(randomize_algorithm))

    try:
        decoded_base64_encrypted_message = base64.b64decode(''.join(decrypted_message_list))

    except (TypeError, ValueError, UnicodeDecodeError) as e:
        print('KEY ERROR: ', e)
        print()
        return

    for character_enumeration_number, encrypted_letters in enumerate(decoded_base64_encrypted_message.decode('utf-8')):
        message_characters = ord(encrypted_letters)
        key_characters = ord(key[character_enumeration_number % len(key)])

        randomize_algorithm = int((message_characters / 2) / key_characters)
        base64_decrypted_message_list.append(chr(randomize_algorithm))

    print()
    print('KEY INPUT: ', key)
    separator()
    print('DECRYPTED MESSAGE: ')
    print()
    print(textwrap.fill(''.join(base64_decrypted_message_list), 100))
    separator()


def rotate_rotor(character_set, rotations):
    return character_set[rotations:] + character_set[:rotations]


def separator():
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
