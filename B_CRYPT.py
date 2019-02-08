def input_message():
    encrypted_msg = []
    decrypted_msg = []

    print()
    in_mess = input("ENTER MESSAGE:")
    print()
    in_key = input("ENTER KEY:")
    key = in_key
    print()

    for enum, chars in enumerate(in_mess):
        msg_chars = ord(chars)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = msg_chars * key_chars
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum, ",", "CHARACTER ORDER #: ", msg_chars)
        encrypted_msg.append(chr(randomize_alg))

    for enum, encrypted_letters in enumerate(encrypted_msg):
        msg_chars = ord(encrypted_letters)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = int(msg_chars / key_chars)
        decrypted_msg.append(chr(randomize_alg))

    print()
    print("MESSAGE INPUT:", in_mess)
    print()
    print("KEY INPUT:", key)
    print()
    print('-' * 50)
    print()
    print("ENCRYPTED MESSAGE:", encrypted_msg)
    print()
    for enum, encrypted_chars in enumerate(encrypted_msg):
        print("ENCRYPTED MESSAGE CHARACTER #'s:", enum, "- ", ord(encrypted_chars))
    print()
    print('-' * 50)
    print()
    print("DECRYPTED MESSAGE:", repr(decrypted_msg))


input_message()
