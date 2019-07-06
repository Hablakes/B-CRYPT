import os
import random
import textwrap
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
    print('*** TESTING BRANCH ***')
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

    try:
        if int(user_input) == 1:
            encrypt_message()
        elif int(user_input) == 2:
            decrypt_message()
        elif int(user_input) == 3:
            exit()

    except ValueError as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')


def encrypt_message():
    encrypted_message_list = []
    semantic_encryption_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO ENCRYPT: ', font='cybermedium'))

    separator()

    message = input('ENTER MESSAGE: ')
    separator()
    key = input('ENTER KEY: ')

    separator()

    message_length_integer = int(len(message))
    key_length_integer = int(len(key))
    added_length_integer = message_length_integer + key_length_integer
    multiplied_length_integer = message_length_integer * key_length_integer

    current_time = int(time.time())
    time_bit = abs(current_time) % 1000
    time_bit_length = int(len(str(time_bit)))

    for character_enumeration_number, character in enumerate(message):
        message_character_ordinal = int(ord(character))
        key_enumeration_ordinal = int(ord(key[character_enumeration_number % len(key)]))
        multiplied_message_integer = int(message_character_ordinal * key_enumeration_ordinal)
        encrypted_message_list.append(multiplied_message_integer)

    for multiplied_numbers in encrypted_message_list:
        pseudo_random_multiplied_numbers = multiplied_numbers + time_bit
        semantic_encryption_list.append(pseudo_random_multiplied_numbers)

    encrypted_number_lengths = [len(str(i)) for i in semantic_encryption_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    time_bit_obscurer_length = int(average_encrypted_number_length - time_bit_length)
    time_bit_obscurer_random_number = random_number_with_obscurer_digits(time_bit_obscurer_length)
    time_bit_obscurer = int(str(time_bit) + str(time_bit_obscurer_random_number))

    semantic_encryption_list.append(time_bit_obscurer)
    rotated_semantic_encryption_list = rotate_rotor(semantic_encryption_list, average_encrypted_number_length)
    encrypted_file_path = os.path.expanduser(r'~/{0}').format('Encrypted Message.bc')

    print('*** TEST RESULTS ***')
    print(time_bit, time_bit_obscurer)
    print()
    print(encrypted_message_list)
    print(semantic_encryption_list)
    print(rotated_semantic_encryption_list)
    separator()

    with open(encrypted_file_path, 'w', encoding='utf-8') as f:
        for rotated_encrypted_numbers in rotated_semantic_encryption_list:
            f.write(str(int(rotated_encrypted_numbers)))
            f.write('\n')
        f.close()

    print(pyfiglet.figlet_format('FILE ENCRYPTED SUCCESSFULLY', font='cybermedium'))

    separator()

    print('ENCRYPTED FILE LOCATION: ' + os.path.abspath(encrypted_file_path))


def decrypt_message():
    encrypted_numbers_list = []
    rotated_encrypted_file_list = []
    semantic_encrypted_file_list = []
    decrypted_file_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO DECRYPT: ', font='cybermedium'))

    separator()

    user_file = tk_gui_file_selection_window()
    user_file_filename = user_file.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print('FILE SELECTED: ', user_file_filename)
    separator()
    key = input('ENTER KEY: ')

    separator()

    with open(user_file, encoding='utf-8') as f:
        for encrypted_numbers in f:
            encrypted_numbers_list.append(int(encrypted_numbers.rstrip('\n')))

    encrypted_number_lengths = [len(str(i)) for i in encrypted_numbers_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    inverse_average_encrypted_number_length = (average_encrypted_number_length - (average_encrypted_number_length * 2))

    rotated_encrypted_file = rotate_rotor(encrypted_numbers_list, inverse_average_encrypted_number_length)

    for characters in rotated_encrypted_file:
        rotated_encrypted_file_list.append(characters)

    for character_enumeration_number, character in enumerate(semantic_encrypted_file_list):
        message_character_integer = int(character)
        key_enumeration_ordinal = int(ord(key[character_enumeration_number % len(key)]))
        divided_message_integer = int(message_character_integer // key_enumeration_ordinal)
        decrypted_file_list.append(chr(divided_message_integer))

    print()
    print('KEY INPUT: ', key)
    separator()
    print('DECRYPTED MESSAGE: ')
    print()
    print(textwrap.fill(''.join(decrypted_file_list), 100))


def random_number_with_obscurer_digits(number_of_digits):
    number_range_start = 10 ** (number_of_digits - 1)
    number_range_end = (10 ** number_of_digits) - 1
    return random.randint(number_range_start, number_range_end)


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
