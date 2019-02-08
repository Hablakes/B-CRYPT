def rotate_rotor(alphabet, rotations):
    return alphabet[rotations:] + alphabet[:rotations]


def input_message_and_encrypt():
    encrypted_msg = []
    decrypted_msg = []

    print()
    in_mess = input("ENTER MESSAGE:")
    print()
    in_key = input("ENTER KEY:")
    key = in_key
    print()

    for enum, chars in enumerate(in_mess):
        randomize_alg = int(ord(chars) * ord(chars)) - int(enum)
        msg_chars = ord(chars)
        key_chars = ord(key[enum % len(key)])
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum, ",", "CHARACTER ORDER #: ", msg_chars)
        print()
        encrypted_msg.append(msg_chars + (randomize_alg + key_chars))
        print()
        print(encrypted_msg)

    print()
    print("MESSAGE INPUT:", in_mess)
    print()
    print("KEY INPUT:", key)


input_message_and_encrypt()
