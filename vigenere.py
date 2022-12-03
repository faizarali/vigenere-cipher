import sys


def read_file(file_name):
    with open(file_name, 'r') as file_name_arg:
        file_str = file_name_arg.read().replace('\n', '').replace(' ', '')

    # Only need the alphabetic letter, then make them lowercase.
    return ''.join(filter(str.isalpha, file_str)).lower()


def print_to_console(text, limit):
    count = 0

    for char in text:
        print(char, end='')
        # Put a newline when we print up to the limit.
        if (count + 1) % limit == 0:
            print()
        count += 1
    print()


def making_plaintext(plaintext_arg):
    plaintext_arg = read_file(plaintext_arg)

    while len(plaintext_arg) < 512:
        plaintext_arg += 'x'

    if len(plaintext_arg) > 512:
        plaintext_arg = plaintext_arg[:512]

    return plaintext_arg


def modify_key_string(key_string):
    key_init_len = len(key_string)
    key_tracker = 0

    while len(key_string) < 512:
        key_string += key_string[key_tracker]
        key_tracker += 1

        if key_tracker >= key_init_len:
            key_tracker = 0

    return key_string


def building_ciphertext(key_string, plaintext_string):
    cipher_string = ""

    for plaintext_char, key_char in zip(plaintext_string, key_string):
        plaintext_num = ord(plaintext_char) - ord('a')
        key_num = ord(key_char) - ord('a')
        combined_num = (plaintext_num + key_num) % 26
        cipher_string += chr(combined_num + ord('a'))

    return cipher_string


def main():
    if len(sys.argv) != 3:
        print('Usage: python3 vigenere.py keyFile plaintextFile', file=sys.stderr)
        sys.exit(1)

    key_str = read_file(sys.argv[1])

    print()
    print()

    print('Vigenere Key:')
    print()

    print_to_console(key_str, 80)

    print()
    print()

    plaintext_str = making_plaintext(sys.argv[2])

    print('Plaintext:')
    print()

    print_to_console(plaintext_str, 80)

    print()
    print()

    key_str = modify_key_string(key_str)

    cipher_str = building_ciphertext(key_str, plaintext_str)

    print('Ciphertext:')
    print()

    print_to_console(cipher_str, 80)


if __name__ == "__main__":
    main()
