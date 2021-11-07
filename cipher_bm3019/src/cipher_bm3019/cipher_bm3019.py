def cipher(text, shift, encrypt=True):
        """Encrypts and decrypts the alphabet characters in a string, by replacing letters
        with the character found 'shift' value away from original character in alphabet
        included below. Inputs include 'text', which is the text string to encrypt or
        decrypt, 'shift', which is the numerical distance by which to shift
        the original character in the alphabet, and 'encrypt', which when set to True will do
        the encryption, and when set to False, will work backards to undo encryption.
        Example: in: cipher('test', 1, encrypt = True) out: 'uftu'."""
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text