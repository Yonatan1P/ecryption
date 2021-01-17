from english_words import english_words_set

def encrypt(string, shift):

    encrypted_string = ""

    # Range of lower case letters a:97, z:122
    # Range of upper case letters A: 65, Z: 96
    # Range of numbers: 0: 48, 9: 57
    for letter in string:

        order = ord(letter)
        shifted_order = order + shift

        if order < 48:
            shifted_order = order
        elif order < 65 and order > 57:
            shifted_order = order
        elif order > 122:
            shifted_order = order
        elif order >= 48 and order <= 57:
            if shifted_order > 57:
                shifted_order = shifted_order - 10
        elif order < 97 and shifted_order >= 97:
            shifted_order = shifted_order - 26
        elif shifted_order > 122:
            shifted_order = shifted_order - 26
        encrypted_string += chr(shifted_order)

    return encrypted_string

def decrypt(encrypted_string, shift):

    decrypted_string = ""

    for letter in encrypted_string:
        encrypted_order = ord(letter)
        unshifted_order = encrypted_order - shift
        if encrypted_order < 48:
            unshifted_order = encrypted_order
        elif encrypted_order < 65 and encrypted_order > 57:
            unshifted_order = encrypted_order
        elif encrypted_order > 122:
            unshifted_order = encrypted_order
        elif encrypted_order >= 48 and encrypted_order <= 57:
            if unshifted_order < 48:
                unshifted_order = unshifted_order + 10
        elif unshifted_order < 65:
            unshifted_order = unshifted_order + 26
        elif encrypted_order > 96 and unshifted_order < 97:
            unshifted_order = unshifted_order + 26
        decrypted_string += chr(unshifted_order)

    return decrypted_string

def crack(encrypted_string):

    encrypted_words = encrypted_string.split(' ')
    decrypted_string = ''
    for encrypted_word in encrypted_words:
        i = 26
        decrypted_word = ''
        while decrypted_word not in english_words_set:
            decrypted_word = ''
            for letter in encrypted_word:
                encrypted_order = ord(letter)
                print(encrypted_order)
                unshifted_order = encrypted_order - i
                if encrypted_order < 48:
                    unshifted_order = encrypted_order
                elif encrypted_order < 65 and encrypted_order > 57:
                    unshifted_order = encrypted_order
                elif encrypted_order > 122:
                    unshifted_order = encrypted_order
                elif encrypted_order >= 48 and encrypted_order <= 57:
                    if unshifted_order < 48:
                        unshifted_order = unshifted_order + 10
                elif unshifted_order < 65:
                    unshifted_order = unshifted_order + 26
                elif encrypted_order > 96 and unshifted_order < 97:
                    unshifted_order = unshifted_order + 26
                decrypted_word += chr(unshifted_order)
            i = i - 1
        decrypted_string += decrypted_word
    return decrypted_string
