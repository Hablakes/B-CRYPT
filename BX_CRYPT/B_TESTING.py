import time

import pyfiglet
import tkinter
import tkinter.filedialog


def main():
    while True:
        interface()


temp_message = []


def interface():
    separator()
    print(pyfiglet.figlet_format('BX-CRYPT', font='cybermedium'))
    print("*** TESTING BRANCH ***")
    print('-' * 100)
    print()
    print()
    print('SYMMETRICAL KEY ENCRYPTION OPTIONS: ')
    print()
    print('1) ENCRYPT A MESSAGE         2) DECRYPT A MESSAGE')
    print()
    print('3) EXIT')
    separator()
    user_input = input('ENTER OPTION #: ')
    separator()

    if int(user_input) == 1:
        encrypt_message()
    elif int(user_input) == 2:
        decrypt_message()
    elif int(user_input) == 3:
        exit()


def encrypt_message():
    encrypted_message_list = []
    semantic_encryption_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO ENCRYPT: ', font='cybermedium'))

    separator()

    message = input('ENTER MESSAGE: ')
    separator()
    key = input('ENTER KEY: ')

    separator()

    for character_enumeration_number, character in enumerate(message):
        message_character_ordinal = ord(character)
        key_enumeration_ordinal = ord(key[character_enumeration_number % len(key)])
        multiplied_message_integer = int(message_character_ordinal * key_enumeration_ordinal)
        encrypted_message_list.append(multiplied_message_integer)

    message_length_integer = int(len(message))
    key_length_integer = int(len(key))
    added_length_integer = message_length_integer + key_length_integer
    multiplied_length_integer = message_length_integer * key_length_integer
    current_time = int(time.time())
    time_bit = abs(current_time) % 100

    for multiplied_numbers in encrypted_message_list:
        pseudo_random_multiplied_numbers = multiplied_numbers + time_bit
        semantic_encryption_list.append(pseudo_random_multiplied_numbers)
        temp_message.append(pseudo_random_multiplied_numbers)

    print(encrypted_message_list)
    separator()
    print(message_length_integer, key_length_integer, added_length_integer, multiplied_length_integer, current_time,
          time_bit)
    separator()
    print(semantic_encryption_list)


def decrypt_message():
    pass


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
