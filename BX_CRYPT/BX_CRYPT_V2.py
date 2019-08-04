import os
import random
import string
import time

import pyfiglet
from tkinter import filedialog, Tk


def main():
    while True:
        interface()


def interface():
    separator_3()
    print(pyfiglet.figlet_format('BX-CRYPT', font='cybermedium'))
    separator_1()
    print('\n', '\n', 'ENCRYPTION OPTIONS: ', '\n', '\n', '1) ENCRYPT A MESSAGE         2) DECRYPT A MESSAGE', '\n',
          '\n', '3) ENCRYPT A FILE            4) DECRYPT A FILE', '\n', '\n', '5) EXIT')
    separator_3()
    user_input = input('ENTER OPTION #: ')
    separator_3()
    try:
        if int(user_input) == 1:
            encrypt_ui(interface_selection=1)
        elif int(user_input) == 2:
            decrypt_ui(interface_selection=1)
        elif int(user_input) == 3:
            encrypt_ui(interface_selection=2)
        elif int(user_input) == 4:
            decrypt_ui(interface_selection=2)
        elif int(user_input) == 5:
            exit()
    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e, '\n', ('-' * 100), '\n', 'INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return


def encrypt_ui(interface_selection):
    file_bytes_list = []
    key_list = []
    user_file_filename_list = []
    try:
        if int(interface_selection) == 1:
            print(pyfiglet.figlet_format('ENTER MESSAGE TO ENCRYPT: ', font='cybermedium'))
            separator_3()
            message = input('ENTER MESSAGE: ')
            for message_bytes in bytes(message.encode('utf-8')):
                file_bytes_list.append(message_bytes)
        elif int(interface_selection) == 2:
            print(pyfiglet.figlet_format('INPUT FILE TO ENCRYPT: ', font='cybermedium'))
            separator_3()
            user_file = tk_gui_file_selection_window()
            user_file_filename = user_file.rsplit('/', 1)[-1]
            user_file_filename_list.append(user_file_filename)
            print('FILE SELECTED: ', user_file_filename)
            for file_bytes in get_bytes_from_files(user_file):
                file_bytes_list.append(file_bytes)
    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e, '\n', ('-' * 100), '\n', 'INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return
    file_bytes_length = int(len(file_bytes_list))
    separator_3()
    print('SYMMETRICAL KEY OPTIONS: ', '\n', '\n', '1) USE CUSTOM KEY            2) CREATE ONE TIME PAD')
    separator_3()
    key = input('ENTER OPTION #: ')
    separator_3()
    try:
        if int(key) == 1:
            key = input('ENTER KEY: ')
            key_list.append(key)
        elif int(key) == 2:
            one_time_pad_file_path = os.path.expanduser(r'~/{0}').format('ENCRYPTED_MESSAGE.bxk')
            key_list.append(random_string_with_one_time_pad_characters(file_bytes_length))
            with open(one_time_pad_file_path, 'w', encoding='utf-8') as f:
                for key_characters in key_list:
                    f.write(key_characters)
            print('KEY FILE LOCATION: ', os.path.abspath(one_time_pad_file_path))
    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e, '\n', ('-' * 100), '\n', 'INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return
    separator_3()
    rotated_semantic_encryption_list = encrypt_function(key_list, file_bytes_list)
    if int(interface_selection) == 1:
        encrypted_file_path = os.path.expanduser(r'~/{0}').format('ENCRYPTED_MESSAGE.bxc')
        with open(encrypted_file_path, 'w', encoding='utf-8') as f:
            for rotated_encrypted_numbers in rotated_semantic_encryption_list:
                f.write(str(int(rotated_encrypted_numbers)))
                f.write('\n')
            f.close()
        print(pyfiglet.figlet_format('MESSAGE ENCRYPTED SUCCESSFULLY', font='cybermedium'))
        separator_3()
        print('ENCRYPTED FILE LOCATION: ' + os.path.abspath(encrypted_file_path))
    elif int(interface_selection) == 2:
        encrypted_file_path = os.path.expanduser(r'~/{0}').format(user_file_filename_list[0]) + '.bxc'
        with open(encrypted_file_path, 'w', encoding='utf-8') as f:
            for encrypted_numbers in rotated_semantic_encryption_list:
                f.write(str(int(encrypted_numbers)))
                f.write('\n')
            f.close()
        print(pyfiglet.figlet_format('FILE ENCRYPTED SUCCESSFULLY', font='cybermedium'))
        separator_3()
        print('ENCRYPTED FILE LOCATION: ' + os.path.abspath(encrypted_file_path))


def encrypt_function(key_list, file_byte_numbers_list):
    encrypted_numbers_list = []
    semantic_encryption_list = []
    current_time = int(time.time())
    time_bit = int(abs(current_time) % 1000)
    time_bit_length = int(len(str(time_bit)))
    multiplier_bit = int(random_number_for_multiplier_bit())
    for enumeration_number, file_byte in enumerate(file_byte_numbers_list):
        file_byte_character_ordinal = int(file_byte)
        key_enumeration_ordinal = int(ord(''.join(key_list)[enumeration_number % len(''.join(key_list))]))
        multiplied_file_bytes_number_integer = int(
            (file_byte_character_ordinal * key_enumeration_ordinal) * multiplier_bit)
        encrypted_numbers_list.append(multiplied_file_bytes_number_integer)
    for multiplied_numbers in encrypted_numbers_list:
        pseudo_random_multiplied_numbers = int(multiplied_numbers + (time_bit * multiplier_bit))
        semantic_encryption_list.append(pseudo_random_multiplied_numbers)
    encrypted_number_lengths = [len(str(x)) for x in semantic_encryption_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    time_bit_obscurer_length = int(average_encrypted_number_length - time_bit_length)
    time_bit_obscurer_random_number = random_number_with_obscurer_digits(time_bit_obscurer_length)
    obscurer_bits = int(str(time_bit) + str(multiplier_bit) + str(time_bit_obscurer_random_number))
    semantic_encryption_list.append(obscurer_bits)
    rotated_semantic_encryption_list = rotate_list_as_rotor(semantic_encryption_list, average_encrypted_number_length)
    return rotated_semantic_encryption_list


def decrypt_ui(interface_selection):
    key_list = []
    key_filename_list = []
    print(pyfiglet.figlet_format('ENTER FILE TO DECRYPT: ', font='cybermedium'))
    separator_3()
    user_file = tk_gui_file_selection_window()
    user_file_original_filename = user_file.rsplit('/', 1)[-1]
    print('ENCRYPTED FILE SELECTED: ', user_file_original_filename)
    separator_3()
    print('SYMMETRICAL KEY OPTIONS: ', '\n', '\n', '1) USE CUSTOM KEY            2) IMPORT ONE TIME PAD')
    separator_3()
    key = input('ENTER OPTION #: ')
    separator_3()
    try:
        if int(key) == 1:
            key = input('ENTER KEY: ')
            key_list.append(key)
            separator_3()
        elif int(key) == 2:
            key_file = tk_gui_file_selection_window()
            key_filename = key_file.rsplit('/', 1)[-1]
            key_filename_list.append(key_filename)
            with open(key_file, 'r', encoding='utf-8') as f:
                for key_characters in f:
                    key_list.append(key_characters)
    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e, '\n', ('-' * 100), '\n', 'INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return
    decrypted_file_bytes_list = decrypt_function(key_list, user_file)
    try:
        if int(interface_selection) == 1:
            decrypted_message_list = []
            print('KEY SELECTED: ', key_filename_list[0])
            separator_3()
            print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
            separator_3()
            print('DECRYPTED MESSAGE: ', '\n', '\n')
            for decrypted_numbers in decrypted_file_bytes_list:
                decrypted_message_list.append(chr(decrypted_numbers))
            print(''.join(decrypted_message_list))
        elif int(interface_selection) == 2:
            decrypted_file_path = os.path.expanduser(r'~/{0}').format(user_file_original_filename)
            try:
                with open(decrypted_file_path, 'wb') as f:
                    f.write(bytearray(decrypted_file_bytes_list))
            except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
                print("KEY ERROR: ", e, '\n')
                return
            print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
            separator_3()
            print('DECRYPTED FILE LOCATION: ' + os.path.abspath(decrypted_file_path))
    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e, '\n', ('-' * 100), '\n', 'INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return


def decrypt_function(key_list, user_file):
    encrypted_numbers_list = []
    rotated_encrypted_file_list = []
    semantic_encrypted_file_list = []
    decrypted_file_list = []
    with open(user_file, encoding='utf-8') as f:
        for encrypted_numbers in f:
            encrypted_numbers_list.append(int(encrypted_numbers.rstrip('\n')))
    encrypted_number_lengths = [len(str(x)) for x in encrypted_numbers_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    inverse_average_encrypted_number_length = (average_encrypted_number_length - (average_encrypted_number_length * 2))
    rotated_encrypted_file = rotate_list_as_rotor(encrypted_numbers_list, inverse_average_encrypted_number_length)
    for file_byte_numbers in rotated_encrypted_file:
        rotated_encrypted_file_list.append(file_byte_numbers)
    obscurer_bits = rotated_encrypted_file_list.pop()
    time_bit = int(str(obscurer_bits)[:3])
    multiplier_bit = int(str(obscurer_bits)[3])
    for multiplied_numbers in rotated_encrypted_file_list:
        pseudo_random_multiplied_numbers = int(multiplied_numbers - (time_bit * multiplier_bit))
        semantic_encrypted_file_list.append(pseudo_random_multiplied_numbers)
    for enumeration_number, character in enumerate(semantic_encrypted_file_list):
        file_byte_character_integer = int(character)
        key_enumeration_ordinal = int(ord(''.join(key_list)[enumeration_number % len(''.join(key_list))]))
        divided_file_byte_integer = int((file_byte_character_integer // key_enumeration_ordinal) // multiplier_bit)
        decrypted_file_list.append(divided_file_byte_integer)
    return decrypted_file_list


def get_bytes_from_files(filename):
    try:
        with open(filename, 'rb') as f:
            for byte in f.read():
                yield byte
    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e, '\n', ('-' * 100), '\n', 'INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return


def random_number_for_multiplier_bit():
    multiplier_digit = random.randint(1, 9)
    return int((multiplier_digit % 9) + 1)


def random_number_with_obscurer_digits(number_of_digits):
    number_range_start = 10 ** (number_of_digits - 1)
    number_range_end = (10 ** number_of_digits) - 1
    return random.randint(number_range_start, number_range_end)


def random_string_with_one_time_pad_characters(number_of_characters):
    one_time_pad_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(one_time_pad_characters) for _ in range(number_of_characters))


def rotate_list_as_rotor(character_set, rotations):
    return character_set[rotations:] + character_set[:rotations]


def separator_1():
    print('-' * 100)


def separator_3():
    for item in '\n', '-' * 100, '\n':
        print(item)


def tk_gui_file_selection_window():
    root = Tk()
    root.withdraw()
    root.update()
    selected_file = filedialog.askopenfilename()
    root.destroy()
    return selected_file


if __name__ == '__main__':
    main()
