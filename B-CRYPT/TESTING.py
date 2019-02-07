def encrypt(key, msg):
    encrypted_msg = []
    for enum, chars in enumerate(msg):
        key_c = ord(key[enum % len(key)])
        msg_c = ord(chars)
        encrypted_msg.append(chr((msg_c + key_c) % 127))
    return ''.join(encrypted_msg)


def decrypt(key, encrypted):
    decrypt_msg = []
    for enum, chars in enumerate(encrypted):
        key_c = ord(key[enum % len(key)])
        enc_c = ord(chars)
        decrypt_msg.append(chr((enc_c - key_c) % 127))
    return ''.join(decrypt_msg)


if __name__ == '__main__':
    key = 'Blair'
    msg = input(":")
    encrypted = encrypt(key, msg)
    decrypted = decrypt(key, encrypted)

    print('Message:', repr(msg))
    print('Key:', repr(key))
    print('Encrypted:', repr(encrypted))
    print('Decrypted:', repr(decrypted))
