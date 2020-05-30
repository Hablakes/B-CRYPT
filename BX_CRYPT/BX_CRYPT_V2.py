import os
import random
import string
import textwrap
import time

import pyfiglet
import tkinter
import tkinter.filedialog


def main():
    while True:
        interface()


def interface():
    separator()

    print(pyfiglet.figlet_format('BX-CRYPT', font='cybermedium'))
    print('-' * 100)
    print()
    print()
    print('ENCRYPTION OPTIONS: ')
    print()
    print('1) ENCRYPT A MESSAGE         2) DECRYPT A MESSAGE')
    print()
    print('3) ENCRYPT A FILE            4) DECRYPT A FILE')
    print()
    print('5) EXIT')

    separator()

    user_input = input('ENTER OPTION #: ')

    separator()

    try:
        if int(user_input) == 1:
            encrypt_message()
        elif int(user_input) == 2:
            decrypt_message()
        elif int(user_input) == 3:
            encrypt_file()
        elif int(user_input) == 4:
            decrypt_file()
        elif int(user_input) == 5:
            exit()

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return


def encrypt_message():
    message_list = []
    key_list = []
    encrypted_message_list = []
    semantic_encryption_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO ENCRYPT: ', font='cybermedium'))

    separator()

    message = input('ENTER MESSAGE: ')

    for message_characters in message:
        message_list.append(message_characters)

    message_length = int(len(message_list))

    separator()

    print('SYMMETRICAL KEY OPTIONS: ')
    print()
    print('1) USE CUSTOM KEY            2) CREATE ONE TIME PAD')

    separator()

    user_key_input = input('ENTER OPTION #: ')

    separator()

    try:
        if int(user_key_input) == 1:
            key = input('ENTER KEY: ')
            key_list.append(key)

        elif int(user_key_input) == 2:
            one_time_pad_file_path = os.path.expanduser(r'~/{0}').format('ENCRYPTED_MESSAGE.bxk')
            key_list.append(random_string_with_one_time_pad_characters(message_length))

            with open(one_time_pad_file_path, 'w', encoding='utf-8') as f:
                for key_characters in key_list:
                    f.write(key_characters)

            print('KEY FILE LOCATION: ', os.path.abspath(one_time_pad_file_path))

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return

    separator()

    current_time = int(time.time())
    time_bit = int(abs(current_time) % 1000)
    time_bit_length = int(len(str(time_bit)))
    multiplier_bit = int(random_number_for_multiplier_bit())

    for character_enumeration_number, character in enumerate(message_list):
        message_character_ordinal = ord(character)
        key_enumeration_ordinal = int(ord(''.join(key_list)[character_enumeration_number % len(''.join(key_list))]))
        multiplied_message_integer = int((message_character_ordinal * key_enumeration_ordinal) * multiplier_bit)
        encrypted_message_list.append(multiplied_message_integer)

    for multiplied_numbers in encrypted_message_list:
        pseudo_random_multiplied_numbers = int(multiplied_numbers + (time_bit * multiplier_bit))
        semantic_encryption_list.append(pseudo_random_multiplied_numbers)

    encrypted_number_lengths = [len(str(x)) for x in semantic_encryption_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    time_bit_obscurer_length = int(average_encrypted_number_length - time_bit_length)
    time_bit_obscurer_random_number = random_number_with_obscurer_digits(time_bit_obscurer_length)
    obscurer_bits = int(str(time_bit) + str(multiplier_bit) + str(time_bit_obscurer_random_number))

    semantic_encryption_list.append(obscurer_bits)
    rotated_semantic_encryption_list = rotate_list_as_rotor(semantic_encryption_list, average_encrypted_number_length)
    encrypted_file_path = os.path.expanduser(r'~/{0}').format('ENCRYPTED_MESSAGE.bxc')

    with open(encrypted_file_path, 'w', encoding='utf-8') as f:
        for rotated_encrypted_numbers in rotated_semantic_encryption_list:
            f.write(str(int(rotated_encrypted_numbers)))
            f.write('\n')
        f.close()

    print(pyfiglet.figlet_format('MESSAGE ENCRYPTED SUCCESSFULLY', font='cybermedium'))

    separator()

    print('ENCRYPTED FILE LOCATION: ' + os.path.abspath(encrypted_file_path))


def decrypt_message():
    key_list = []
    encrypted_numbers_list = []
    rotated_encrypted_file_list = []
    semantic_encrypted_file_list = []
    decrypted_file_list = []

    print(pyfiglet.figlet_format('ENTER MESSAGE TO DECRYPT: ', font='cybermedium'))

    separator()

    user_file = tk_gui_file_selection_window()
    user_file_original_filename = user_file.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print('FILE SELECTED: ', user_file_original_filename)

    separator()

    print('SYMMETRICAL KEY OPTIONS: ')
    print()
    print('1) USE CUSTOM KEY            2) IMPORT ONE TIME PAD')

    separator()

    user_key_input = input('ENTER OPTION #: ')

    separator()

    try:
        if int(user_key_input) == 1:
            key = input('ENTER KEY: ')
            key_list.append(key)
            separator()

        elif int(user_key_input) == 2:
            key_file = tk_gui_file_selection_window()

            with open(key_file, 'r', encoding='utf-8') as f:
                for key_characters in f:
                    key_list.append(key_characters)

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return

    with open(user_file, encoding='utf-8') as f:
        for encrypted_numbers in f:
            encrypted_numbers_list.append(int(encrypted_numbers.rstrip('\n')))

    encrypted_number_lengths = [len(str(x)) for x in encrypted_numbers_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    inverse_average_encrypted_number_length = (average_encrypted_number_length - (average_encrypted_number_length * 2))

    rotated_encrypted_file = rotate_list_as_rotor(encrypted_numbers_list, inverse_average_encrypted_number_length)

    for characters in rotated_encrypted_file:
        rotated_encrypted_file_list.append(characters)

    obscurer_bits = rotated_encrypted_file_list.pop()
    time_bit = int(str(obscurer_bits)[:3])
    multiplier_bit = int(str(obscurer_bits)[3])

    for multiplied_numbers in rotated_encrypted_file_list:
        pseudo_random_multiplied_numbers = int(multiplied_numbers - (time_bit * multiplier_bit))
        semantic_encrypted_file_list.append(pseudo_random_multiplied_numbers)

    for character_enumeration_number, character in enumerate(semantic_encrypted_file_list):
        message_character_integer = int(character)
        key_enumeration_ordinal = int(ord(''.join(key_list)[character_enumeration_number % len(''.join(key_list))]))
        divided_message_integer = int((message_character_integer // key_enumeration_ordinal) // multiplier_bit)
        decrypted_file_list.append(chr(divided_message_integer))

    print(pyfiglet.figlet_format('MESSAGE DECRYPTED SUCCESSFULLY', font='cybermedium'))

    separator()

    print('DECRYPTED MESSAGE: ')
    print()
    print(textwrap.fill(''.join(decrypted_file_list)))


def encrypt_file():
    file_bytes_list = []
    key_list = []
    encrypted_file_bytes_list = []
    semantic_encryption_list = []

    print(pyfiglet.figlet_format('INPUT FILE TO ENCRYPT: ', font='cybermedium'))

    separator()

    user_file = tk_gui_file_selection_window()
    user_file_filename = user_file.rsplit('/', 1)[-1]
    print('FILE SELECTED: ',  user_file_filename)

    separator()

    for file_bytes in get_bytes_from_files(user_file):
        file_bytes_list.append(file_bytes)

    file_bytes_length = int(len(file_bytes_list))

    print('SYMMETRICAL KEY OPTIONS: ')
    print()
    print('1) USE CUSTOM KEY            2) CREATE ONE TIME PAD')

    separator()

    user_key_input = input('ENTER OPTION #: ')

    separator()

    try:
        if int(user_key_input) == 1:
            key = input('ENTER KEY: ')
            key_list.append(key)

        elif int(user_key_input) == 2:
            one_time_pad_file_path = os.path.expanduser(r'~/{0}').format(user_file_filename + '.bxk')

            key_list.append(random_string_with_one_time_pad_characters(file_bytes_length))

            with open(one_time_pad_file_path, 'w', encoding='utf-8') as f:
                for key_characters in key_list:
                    f.write(key_characters)

            print('KEY FILE LOCATION: ', os.path.abspath(one_time_pad_file_path))

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return

    separator()

    current_time = int(time.time())
    time_bit = int(abs(current_time) % 1000)
    time_bit_length = int(len(str(time_bit)))
    multiplier_bit = int(random_number_for_multiplier_bit())

    for character_enumeration_number, character in enumerate(file_bytes_list):
        message_character_ordinal = int(character)
        key_enumeration_ordinal = int(ord(''.join(key_list)[character_enumeration_number % len(''.join(key_list))]))
        multiplied_message_integer = int((message_character_ordinal * key_enumeration_ordinal) * multiplier_bit)
        encrypted_file_bytes_list.append(multiplied_message_integer)

    for multiplied_numbers in encrypted_file_bytes_list:
        pseudo_random_multiplied_numbers = int(multiplied_numbers + (time_bit * multiplier_bit))
        semantic_encryption_list.append(pseudo_random_multiplied_numbers)

    encrypted_number_lengths = [len(str(x)) for x in semantic_encryption_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    time_bit_obscurer_length = int(average_encrypted_number_length - time_bit_length)
    time_bit_obscurer_random_number = random_number_with_obscurer_digits(time_bit_obscurer_length)
    obscurer_bits = int(str(time_bit) + str(multiplier_bit) + str(time_bit_obscurer_random_number))

    semantic_encryption_list.append(obscurer_bits)
    rotated_semantic_encryption_list = rotate_list_as_rotor(semantic_encryption_list, average_encrypted_number_length)
    encrypted_file_path = os.path.expanduser(r'~/{0}').format(user_file_filename) + '.bxc'

    with open(encrypted_file_path, 'w', encoding='utf-8') as f:
        for encrypted_numbers in rotated_semantic_encryption_list:
            f.write(str(int(encrypted_numbers)))
            f.write('\n')
        f.close()

    print(pyfiglet.figlet_format('FILE ENCRYPTED SUCCESSFULLY', font='cybermedium'))

    separator()

    print('ENCRYPTED FILE LOCATION: ' + os.path.abspath(encrypted_file_path))


def decrypt_file():
    key_list = []
    encrypted_numbers_list = []
    rotated_encrypted_file_bytes_list = []
    semantic_encrypted_file_bytes_list = []
    decrypted_file_bytes_list = []

    print(pyfiglet.figlet_format('INPUT FILE TO DECRYPT: ', font='cybermedium'))

    separator()

    user_file = tk_gui_file_selection_window()
    user_file_original_filename = user_file.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print('FILE SELECTED: ', user_file_original_filename)

    separator()

    print('SYMMETRICAL KEY OPTIONS: ')
    print()
    print('1) USE CUSTOM KEY            2) IMPORT ONE TIME PAD')

    separator()

    user_key_input = input('ENTER OPTION #: ')

    separator()

    try:
        if int(user_key_input) == 1:
            key = input('ENTER KEY: ')
            key_list.append(key)
            separator()

        elif int(user_key_input) == 2:
            key_file = tk_gui_file_selection_window()

            with open(key_file, 'r', encoding='utf-8') as f:
                for key_characters in f:
                    key_list.append(key_characters)

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
        return

    with open(user_file, encoding='utf-8') as f:
        for encrypted_numbers in f:
            encrypted_numbers_list.append(int(encrypted_numbers.rstrip('\n')))

    encrypted_number_lengths = [len(str(x)) for x in encrypted_numbers_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    inverse_average_encrypted_number_length = (average_encrypted_number_length - (average_encrypted_number_length * 2))

    rotated_encrypted_file = rotate_list_as_rotor(encrypted_numbers_list, inverse_average_encrypted_number_length)

    for characters in rotated_encrypted_file:
        rotated_encrypted_file_bytes_list.append(characters)

    obscurer_bits = rotated_encrypted_file_bytes_list.pop()
    time_bit = int(str(obscurer_bits)[:3])
    multiplier_bit = int(str(obscurer_bits)[3])

    for multiplied_numbers in rotated_encrypted_file_bytes_list:
        pseudo_random_multiplied_numbers = int(multiplied_numbers - (time_bit * multiplier_bit))
        semantic_encrypted_file_bytes_list.append(pseudo_random_multiplied_numbers)

    for character_enumeration_number, character in enumerate(semantic_encrypted_file_bytes_list):
        message_character_integer = int(character)
        key_enumeration_ordinal = int(ord(''.join(key_list)[character_enumeration_number % len(''.join(key_list))]))
        divided_message_integer = int((message_character_integer // key_enumeration_ordinal) // multiplier_bit)
        decrypted_file_bytes_list.append(divided_message_integer)

    decrypted_file_path = os.path.expanduser(r'~/{0}').format(user_file_original_filename)

    try:
        with open(decrypted_file_path, 'wb') as f:
            f.write(bytearray(decrypted_file_bytes_list))

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print("KEY ERROR: ", e)
        print()
        return

    print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))

    separator()

    print('DECRYPTED FILE LOCATION: ' + os.path.abspath(decrypted_file_path))


def get_bytes_from_files(filename):
    try:
        with open(filename, 'rb') as f:
            for byte in f.read():
                yield byte

    except (TypeError, ValueError, UnicodeDecodeError, ZeroDivisionError) as e:
        print(e)
        separator()
        print('INPUT ERROR, PLEASE RETRY SELECTION USING NUMBER KEYS: ')
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
