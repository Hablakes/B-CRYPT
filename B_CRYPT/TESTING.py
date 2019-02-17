import base64


def input_message_and_encrypt():
    encrypted_msg = []

    in_msg = input("ENTER MESSAGE TO ENCRYPT:")
    print()
    in_key = input("ENTER KEY:")
    key = in_key
    print()
    print('-' * 80)
    print()

    for enum, chars in enumerate(in_msg):
        msg_chars = ord(chars)
        key_chars = ord(key[enum % len(key)])
        randomize_alg = (msg_chars * 2) * key_chars
        print("CHARACTER: ", chars, ":", "ENUMERATION #: ", enum, ",", "CHARACTER ORDER #: ", msg_chars)
        encrypted_msg.append(chr(randomize_alg))

    print()
    print("MESSAGE INPUT:", in_msg)
    print()
    print("KEY INPUT:", key)
    print()
    print('-' * 80)
    print()
    print("ENCRYPTED MESSAGE:", ''.join(encrypted_msg))
    print()

    encrypted_msg_bytes = ''.join(encrypted_msg).encode("utf-8")
    encoded_b64_encrypted_msg = base64.b64encode(encrypted_msg_bytes)

    print("BASE 64 ENCODED ENCRYPTED MESSAGE:", encoded_b64_encrypted_msg.decode('utf-8'))

    decoded_b64_encrypted_msg = base64.b64decode(encoded_b64_encrypted_msg)

    print()
    print("BASE 64 DECODED ENCRYPTED MESSAGE:", decoded_b64_encrypted_msg.decode('utf-8'))
    print()


input_message_and_encrypt()
