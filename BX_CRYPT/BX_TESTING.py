import os
import random
import string
import textwrap
import time

import pyfiglet
import tkinter
import tkinter.filedialog


def encrypt_file():

    current_time = int(time.time())
    time_bit = int(abs(current_time) % 1000)
    time_bit_length = int(len(str(time_bit)))
    multiplier_bit = int(abs(current_time) % 10)
    if multiplier_bit == 0:
        multiplier_bit = int(multiplier_bit + 1)

    print(multiplier_bit)


def random_string_with_one_time_pad_characters(number_of_characters):
    one_time_pad_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(one_time_pad_characters) for x in range(number_of_characters))


def random_number_with_obscurer_digits(number_of_digits):
    number_range_start = 10 ** (number_of_digits - 1)
    number_range_end = (10 ** number_of_digits) - 1
    return random.randint(number_range_start, number_range_end)


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


encrypt_file()
