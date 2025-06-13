def decrypt(text, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
    
    decrypted_text = ''
    for char in text:
        upper_char = char.upper()
        if upper_char in key:
            index = key.index(upper_char)
            original = alphabet[index]
            decrypted_text += original
        else:
            decrypted_text += char
    return decrypted_text