"""
    str(chr(0xd800))

    encoding='utf-8', errors='replace')

    .encode(bytes)
    .encode('utf-8', 'replace')
    .decode(bytes)
    .decode('utf-8', 'surrogateescape'))
    .decode('utf-8', 'surrogatepass'))

    with open(os.path.expanduser(r'~/{0}').format(file_to_encrypt_filename) + '.bc', 'w', encoding='utf-8') as f:
        f.write(''.join(encrypted_file))

    print()
    print(pyfiglet.figlet_format("FILE ENCRYPTED SUCCESSFULLY", font="cybermedium"))
"""

