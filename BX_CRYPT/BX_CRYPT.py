import base64
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


def interface():
    print('-' * 100)
    print(pyfiglet.figlet_format('BX-CRYPT', font='cybermedium'))
    print('-' * 100)
    print()
    print()
    print('SYMMETRICAL KEY ENCRYPTION OPTIONS: ')
    print()
    print('1) ENCRYPT A MESSAGE         2) DECRYPT A MESSAGE')
    print()
    print('3) ENCRYPT A FILE            4) DECRYPT A FILE')
    print()
    print('5) EXIT')
    separator()
    user_input = input('ENTER OPTION #: ')
    separator()

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

    encrypted_number_lengths = [len(str(x)) for x in semantic_encryption_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    time_bit_obscurer_length = int(average_encrypted_number_length - time_bit_length)
    time_bit_obscurer_random_number = random_number_with_obscurer_digits(time_bit_obscurer_length)
    time_bit_obscurer = int(str(time_bit) + str(time_bit_obscurer_random_number))

    semantic_encryption_list.append(time_bit_obscurer)
    rotated_semantic_encryption_list = rotate_rotor(semantic_encryption_list, average_encrypted_number_length)
    encrypted_file_path = os.path.expanduser(r'~/{0}').format('Encrypted Message.bc')

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

    encrypted_number_lengths = [len(str(x)) for x in encrypted_numbers_list]
    average_encrypted_number_length = int(sum(encrypted_number_lengths) // len(encrypted_number_lengths))
    inverse_average_encrypted_number_length = (average_encrypted_number_length - (average_encrypted_number_length * 2))

    rotated_encrypted_file = rotate_rotor(encrypted_numbers_list, inverse_average_encrypted_number_length)

    for characters in rotated_encrypted_file:
        rotated_encrypted_file_list.append(characters)

    time_bit_obscurer = rotated_encrypted_file_list.pop()
    time_bit = int(str(time_bit_obscurer)[:3])

    for multiplied_numbers in rotated_encrypted_file_list:
        pseudo_random_multiplied_numbers = multiplied_numbers - time_bit
        semantic_encrypted_file_list.append(pseudo_random_multiplied_numbers)

    for character_enumeration_number, character in enumerate(semantic_encrypted_file_list):
        message_character_integer = int(character)
        key_enumeration_ordinal = int(ord(key[character_enumeration_number % len(key)]))
        divided_message_integer = int(message_character_integer // key_enumeration_ordinal)
        decrypted_file_list.append(chr(divided_message_integer))

    print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
    separator()
    print('DECRYPTED MESSAGE: ')
    print()
    print(textwrap.fill(''.join(decrypted_file_list)))


def encrypt_file():
    encrypted_file_list = []
    base64_encrypted_file_list = []

    print(pyfiglet.figlet_format('INPUT FILE TO ENCRYPT: ', font='cybermedium'))
    separator()
    user_file = tk_gui_file_selection_window()
    user_file_filename = user_file.rsplit('/', 1)[-1]
    print('FILE SELECTED: ',  user_file_filename)
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

    for character_enumeration_number, characters in enumerate(get_bytes_from_files(user_file)):
        message_characters = characters
        key_characters = ord(key[character_enumeration_number % len(key)])
        randomize_algorithm = ((message_characters * 2) * key_characters) % 1114100

        encrypted_file_list.append(chr(randomize_algorithm))

    encrypted_file_list_bytes = ''.join(encrypted_file_list).encode('utf-8')
    encoded_base64_encrypted_message = base64.b64encode(encrypted_file_list_bytes)

    for character_enumeration_number, characters in enumerate(encoded_base64_encrypted_message.decode('utf-8')):
        message_characters = ord(characters)
        key_characters = ord(key[character_enumeration_number % len(key)])
        randomize_algorithm = (message_characters * key_spin) * key_characters

        base64_encrypted_file_list.append(randomize_algorithm)

    base64_encrypted_file_list.insert(int(key_spin), int(time_spin))
    rotated_encrypted_file = rotate_rotor(base64_encrypted_file_list, int(len(key)))

    with open(os.path.expanduser(r'~/{0}').format(user_file_filename) + '.bc', 'w', encoding='utf-8') as f:
        for encrypted_numbers in rotated_encrypted_file:
            f.write(str(int(encrypted_numbers)))
            f.write('\n')
        f.close()

    print(pyfiglet.figlet_format('FILE ENCRYPTED SUCCESSFULLY', font='cybermedium'))
    separator()


def decrypt_file():
    encrypted_numbers_list = []
    rotated_encrypted_file_list = []
    base64_decoded_file_list = []
    decrypted_file_list = []

    print(pyfiglet.figlet_format('INPUT FILE TO DECRYPT: ', font='cybermedium'))
    separator()
    user_file = tk_gui_file_selection_window()
    user_file_filename = user_file.rsplit('.', 1)[0].rsplit('/', 1)[-1]
    print('FILE SELECTED: ',  user_file_filename)
    separator()
    key = input('ENTER KEY: ')
    separator()
    key_spin = int(len(key)) % 6
    inverse_key = (int(len(key)) - int(len(key)) * 2)

    if key_spin <= 1:
        key_spin = (key_spin + 2)
    else:
        pass

    with open(user_file, encoding='utf-8') as f:

        for encrypted_numbers in f:
            encrypted_numbers_list.append(chr(int(encrypted_numbers.rstrip('\n'))))

    rotated_encrypted_file = rotate_rotor(''.join(encrypted_numbers_list), int(inverse_key))

    for characters in rotated_encrypted_file:
        rotated_encrypted_file_list.append(characters)

    time_spin_character = rotated_encrypted_file_list.pop(int(key_spin))

    for character_enumeration_number, encrypted_letters in enumerate(rotated_encrypted_file_list):
        message_characters = ord(encrypted_letters)
        key_characters = ord(key[character_enumeration_number % len(key)])
        randomize_algorithm = int((message_characters / key_spin) / key_characters) % 1114100

        base64_decoded_file_list.append(chr(randomize_algorithm))

    try:
        decoded_base64_encrypted_file = base64.b64decode(''.join(base64_decoded_file_list))

    except (TypeError, ValueError, UnicodeDecodeError) as e:
        print('KEY ERROR: ', e)
        print()
        return

    for character_enumeration_number, encrypted_letters in enumerate(decoded_base64_encrypted_file.decode('utf-8')):
        message_characters = ord(encrypted_letters)
        key_characters = ord(key[character_enumeration_number % len(key)])
        randomize_algorithm = int((message_characters / 2) / key_characters)

        decrypted_file_list.append(randomize_algorithm)

    with open(os.path.expanduser(r'~/{0}').format(user_file_filename), 'wb') as f:
        f.write(bytearray(decrypted_file_list))

    print(pyfiglet.figlet_format('FILE DECRYPTED SUCCESSFULLY', font='cybermedium'))
    separator()


def get_bytes_from_files(filename):
    print()
    print('ENTER BYTE AMOUNT (BLOCK SIZE) TO SCAN WITH: ')
    print()
    print('DEFAULT BLOCK SIZE IS 1024 (1KB).  IF UNSURE, ENTER: "1024"')
    separator()
    input_bytes_amount = input('ENTER BYTE AMOUNT: ')
    separator()
    with open(filename, 'rb') as f:
        while True:
            bytes_amount = f.read(int(input_bytes_amount))

            if bytes_amount:

                for bts in bytes_amount:
                    yield bts
            else:
                break


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
