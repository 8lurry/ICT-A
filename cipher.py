import string
letters = string.ascii_lowercase
text = "plagiarism is not allowed"
name = "blurry"
roll = 26

def substitiution_cipher(text=text, key=roll, left_shift=True):
    subs = {}
    if left_shift:
        for i in range(len(text)):
            shift = (i - key) % 26
            shift = shift if shift >= 0 else 26 + shift
            subs[letters[i]] = letters[shift]
    else:
        for i in range(len(text)):
            subs[letters[i]] = letters[(i + key) % 26]
    cipher_text = ""
    for char in text:
        if char in letters:
            cipher_text += subs[char]
        else:
            cipher_text += char
    return cipher_text

def caeser_cipher(text=text, key=3, left_shift=False):
    return substitiution_cipher(text=text, key=key, left_shift=left_shift)

def transposition_cipher(text=text, key=name):
    width = len(key)
    order = [char for char in key]
    count = 0
    for char in letters:
        for i, k in enumerate(order):
            if char == k:
                order[i] = count
                count += 1
    r = len(text) % width
    height = (len(text) // width) + 1 if r != 0 else len(text) // width
    s_text = [char for char in text]
    cipher_text = ""
    for i in range(width):
        for k, ords in enumerate(order):
            if ords == i:
                for j in range(height):
                    try:
                        cipher_text += s_text[k+j*width]
                    except IndexError:
                        cipher_text += " "
    return cipher_text

if __name__ == "__main__":
    print(f"""Ciphers of '{text}'
    Substitution Cipher with {roll} left shift:
    >>>
    >>> {substitiution_cipher()}
    >>>
    Caeser Cipher:
    >>>
    >>> {caeser_cipher()}
    >>>
    Transposition Cipher using lexicographic order of the key '{name}':
    >>>
    >>> {transposition_cipher()}
    >>>""")
