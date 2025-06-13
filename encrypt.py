def encrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
   
    encrypted_text = ''
    for char in text:
        upper_char = char.upper()
        if upper_char in alphabet:
            index = alphabet.index(upper_char)
            replace = key[index]
            encrypted_text += replace
        else:
            encrypted_text += char
    return encrypted_text


